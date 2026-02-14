---
layout: default
title: Interactive 2D Transformation Tool
parent: Projects
permalink: /projects/transformation-tool/
---

# Interactive 2D Transformation Tool

This project demonstrates various 2D geometric transformations: **Translation**, **Rigid** (Rotation + Translation), **Similarity** (Scale + Rotation + Translation), **Affine**, and **Projective** (Homography).

You can interact with the widget below to explore how these transformations affect a 2D shape.

<div style="width: 100%; display: flex; justify-content: center; margin-bottom: 30px;">
    <iframe src="../transformation_widget.html" width="620" height="680" style="border: none; overflow: hidden;"></iframe>
</div>

---

## Source Code (Python)

This tool was originally built in Python using **PySide6** and **NumPy**. Below is the source code for the desktop application.

### `transform.py`
The core logic engine. It handles matrix operations and solves for transformation parameters (including the Homography solver).

```python
import numpy as np 

class TransformationEngine:
    def __init__(self):
        self.matrix = np.eye(3)

    def set_matrix(self, M):
        self.matrix = M

    def get_matrix(self):
        return self.matrix

    def reset(self):
        self.matrix = np.eye(3)

    def compose(self, M):
        self.matrix = M @ self.matrix

    def size(self):
        return self.matrix.shape

    def inverse(self):
        inv = np.linalg.inv(self.matrix)
        self.matrix = inv
        return inv 

    def applyTransform(self, points):
        ones = np.ones((points.shape[0],1))
        homogenous_points = np.hstack([points, ones])
        transformed = homogenous_points @ self.matrix.T
        
        # Perspective division
        w = transformed[:, 2:3]
        return transformed[:, :2] / w

    def set_translation(self, dx, dy):
        self.matrix = np.array([
            [1, 0, dx],
            [0, 1, dy],
            [0, 0, 1]
        ], dtype=float)

    def set_rigid(self, angle_rad,cx,cy):
        cos_theta = np.cos(angle_rad)
        sin_theta = np.sin(angle_rad)

        T1 = np.array([
            [1, 0, -cx],
            [0, 1, -cy],
            [0, 0, 1]
        ], dtype=float)

        R = np.array([
            [cos_theta, -sin_theta, 0],
            [sin_theta, cos_theta, 0],
            [0, 0, 1]
        ], dtype=float)

        T2 = np.array([
            [1, 0, cx],
            [0, 1, cy],
            [0, 0, 1]
        ], dtype=float)

        self.compose(T2 @ R @ T1)

    def set_similarity(self, scale, angle_rad, cx, cy):
        cos_theta = np.cos(angle_rad)
        sin_theta = np.sin(angle_rad)

        T1 = np.array([
            [1, 0, -cx],
            [0, 1, -cy],
            [0, 0, 1]
        ], dtype=float)

        R = np.array([
            [cos_theta, -sin_theta, 0],
            [sin_theta, cos_theta, 0],
            [0, 0, 1]
        ], dtype=float)

        T2 = np.array([
            [1, 0, cx],
            [0, 1, cy],
            [0, 0, 1]
        ], dtype=float)
        
        # Scale
        S = np.array([
            [scale, 0, 0],
            [0, scale, 0],
            [0, 0, 1]
        ], dtype=float)

        M = T2 @ S @ R @ T1
        self.compose(M)

    def set_affine_from_3points(self, src_pts, dst_pts):
        """
        src_pts: (3,2) original triangle
        dst_pts: (3,2) transformed triangle
        """
        # Build linear system
        A = []
        b = []

        for (x, y), (xp, yp) in zip(src_pts, dst_pts):
            A.append([x, y, 1, 0, 0, 0])
            A.append([0, 0, 0, x, y, 1])
            b.append(xp)
            b.append(yp)

        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float)

        params = np.linalg.solve(A, b)

        M = np.array([
            [params[0], params[1], params[2]],
            [params[3], params[4], params[5]],
            [0, 0, 1]
        ])

        self.matrix = M

    def set_projective_from_4points(self, src_pts, dst_pts):
        """
        src_pts: (4,2) original quad
        dst_pts: (4,2) transformed quad
        """
        A = []
        b = []
        
        for (x, y), (xp, yp) in zip(src_pts, dst_pts):
            # h11 x + h12 y + h13 - h31 x xp - h32 y xp = xp
            # h21 x + h22 y + h23 - h31 x yp - h32 y yp = yp
            A.append([x, y, 1, 0, 0, 0, -x*xp, -y*xp])
            A.append([0, 0, 0, x, y, 1, -x*yp, -y*yp])
            b.append(xp)
            b.append(yp)

        A = np.array(A, dtype=float)
        b = np.array(b, dtype=float)

        try:
            params = np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
             # Fallback or handle singular matrix if points are collinear
             return

        # h33 is 1
        M = np.array([
            [params[0], params[1], params[2]],
            [params[3], params[4], params[5]],
            [params[6], params[7], 1.0]
        ])

        self.matrix = M

    def get_type(self, tol=1e-6):
        R = self.matrix[:2,:2]
        bottom = self.matrix[2,:]

        if np.allclose(bottom, [0,0,1], atol=tol):
            if np.allclose(R, np.eye(2), atol=tol):
                return "Translation"
            elif np.allclose(R.T @ R, np.eye(2), atol=tol) and np.isclose(np.linalg.det(R),1,tol):
                return "Rigid"
            elif np.allclose(R[0,0], R[1,1], atol=tol) and np.allclose(R[0,1], -R[1,0], atol=tol):
                return "Similarity"
            else:
                return "Affine"
        else:
            return "Projective"

    def degrees_of_freedom(self):
        t = self.get_type()
        return {"Translation":2, "Rigid":3, "Similarity":4, "Affine":6, "Projective":8}[t]


class ShapeModel:
    def __init__(self):
        self.local_points = np.array([[0,0], [100,0], [100,100], [0,100]], dtype=float)
        self.engine = TransformationEngine()

    def getWorldPoints(self):
        return self.engine.applyTransform(self.local_points)
```

### `canvas.py`
The UI widget using PySide6 `QPainter`.

```python
from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter, QPen
from PySide6.QtCore import Qt
from transform import ShapeModel
import numpy as np

class CanvasWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.mode = "TRANSLATION"
        self.is_dragging = False
        self.start_pos = None
        self.rotation_start_vector = None
        self.active_corner = None
        self.initial_matrix = None
        self.initial_center = None
        self.scale = None
        self.sim_center = None
        self.shape = ShapeModel()

        # initial position
        self.pos_x = 200
        self.pos_y = 200
        self.shape.engine.set_translation(self.pos_x, self.pos_y)

    def get_center(self):
        points = self.shape.getWorldPoints()
        cx = points[:, 0].mean()
        cy = points[:, 1].mean()
        return cx, cy
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), Qt.white)

        pen = QPen(Qt.red, 3)
        painter.setPen(pen)

        points = self.shape.getWorldPoints()

        # Draw rectangle edges
        for i in range(len(points)):
            x1, y1 = points[i]
            x2, y2 = points[(i + 1) % len(points)]
            painter.drawLine(int(x1), int(y1), int(x2), int(y2))

        # Draw corner handles
        for x, y in points:
            painter.drawEllipse(int(x)-4, int(y)-4, 8, 8)

    def get_corner(self, ev_pos):
        mouse_pos = np.array([ev_pos.x(), ev_pos.y()])
        points = self.shape.getWorldPoints()
        
        for i, p in enumerate(points):
            dist = np.linalg.norm(p - mouse_pos)
            if dist < 10:
                return i
        return None

    def mousePressEvent(self, event):
        if self.mode == "RIGID" or self.mode=="SIMILARITY":
            if event.button() == Qt.LeftButton:
                self.is_dragging = True
                self.start_pos = event.pos()
            elif event.button() == Qt.RightButton:
                self.sim_center = self.get_center()
                cx, cy = self.sim_center
                dx = event.x() - cx
                dy = event.y() - cy
                self.rotation_start_vector = np.array([dx, dy], dtype=float)
        else:
            self.active_corner = self.get_corner(event.pos())
            if self.active_corner is not None:
                self.is_dragging = True
                self.start_pos = event.pos()
                if self.mode == "SIMILARITY":
                    self.initial_matrix = self.shape.engine.get_matrix().copy()
                    self.initial_center = self.get_center()
            if event.button() == Qt.LeftButton:
                self.is_dragging = True
                self.start_pos = event.pos()
        if self.mode == "PROJECTIVE" and self.active_corner is not None:
            self.initial_world_pts = self.shape.getWorldPoints().copy()

    def mouseMoveEvent(self, event):
        if not self.is_dragging and self.rotation_start_vector is None:
            return
        current_pos = event.pos()

        if self.mode == "TRANSLATION":
            dx = current_pos.x() - self.start_pos.x()
            dy = current_pos.y() - self.start_pos.y()
            self.pos_x += dx
            self.pos_y += dy
            self.shape.engine.set_translation(self.pos_x, self.pos_y)
            self.start_pos = current_pos

        elif self.mode == "AFFINE":
            if self.active_corner is not None:
                world_pts = self.shape.getWorldPoints()
                indices = [self.active_corner, (self.active_corner + 1) % 4, (self.active_corner + 2) % 4]
                src = self.shape.local_points[indices].copy()
                dst = world_pts[indices].copy()
                dx = current_pos.x() - self.start_pos.x()
                dy = current_pos.y() - self.start_pos.y()
                dst[0] += np.array([dx, dy])
                self.shape.engine.set_affine_from_3points(src, dst)
                self.start_pos = current_pos

        elif self.mode == "RIGID":
            if self.is_dragging:
                dx = current_pos.x() - self.start_pos.x()
                dy = current_pos.y() - self.start_pos.y()
                T = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]])
                self.shape.engine.compose(T)
                self.start_pos = current_pos
            elif self.rotation_start_vector is not None:
                cx, cy = self.get_center()
                current_vector = np.array([event.x() - cx, event.y() - cy], dtype=float)
                dot = np.dot(self.rotation_start_vector, current_vector)
                det = np.cross(self.rotation_start_vector, current_vector)
                angle = np.arctan2(det, dot)
                self.shape.engine.set_rigid(angle, cx, cy)
                self.rotation_start_vector = current_vector

        elif self.mode == "SIMILARITY":
            if self.active_corner is not None:
                # Similarity corner logic omitted for brevity
                pass
            elif self.is_dragging:
                dx = current_pos.x() - self.start_pos.x()
                dy = current_pos.y() - self.start_pos.y()
                T = np.array([[1, 0, dx], [0, 1, dy], [0, 0, 1]], dtype=float)
                self.shape.engine.compose(T)
                self.start_pos = current_pos
            elif self.rotation_start_vector is not None:
                cx, cy = self.sim_center
                current_vector = np.array([event.x() - cx, event.y() - cy], dtype=float)
                v0 = self.rotation_start_vector
                v = current_vector
                norm_v0 = np.linalg.norm(v0)
                norm_v = np.linalg.norm(v)
                if norm_v0 > 1e-6 and norm_v > 1e-6:
                    dot = np.dot(v0, v)
                    det = np.cross(v0, v)
                    angle = np.arctan2(det, dot)
                    scale = norm_v / norm_v0
                    self.shape.engine.set_similarity(scale, angle, cx, cy)
                    self.rotation_start_vector = current_vector

        elif self.mode == "PROJECTIVE":
            if self.active_corner is not None:
                src = self.shape.local_points.copy()
                dst = self.initial_world_pts.copy()
                dx = current_pos.x() - self.start_pos.x()
                dy = current_pos.y() - self.start_pos.y()
                dst[self.active_corner] = self.initial_world_pts[self.active_corner] + np.array([dx, dy])
                self.shape.engine.set_projective_from_4points(src, dst)

        self.update()
    
    def mouseReleaseEvent(self, event):
        self.is_dragging = False
        self.rotation_start_vector = None
        self.active_corner = None

    def setMode(self, mode):
        print("Mode changed to:", mode)
        self.mode = mode

    def reset(self):
        self.pos_x = 200
        self.pos_y = 200
        self.shape.engine.reset()
        self.shape.engine.set_translation(self.pos_x, self.pos_y)
        self.update()
```

### `main.py`
The application entry point.

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from canvas import CanvasWidget
import sys

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.canvas = CanvasWidget()

        # Buttons
        btn_translation = QPushButton("Translation")
        btn_rigid = QPushButton("Rigid")
        btn_similarity = QPushButton("Similarity")
        btn_affine = QPushButton("Affine")
        btn_perspective = QPushButton("Projective")
        btn_reset = QPushButton("Reset")

        # Connect buttons
        btn_translation.clicked.connect(lambda: self.canvas.setMode("TRANSLATION"))
        btn_rigid.clicked.connect(lambda: self.canvas.setMode("RIGID"))
        btn_similarity.clicked.connect(lambda: self.canvas.setMode("SIMILARITY"))
        btn_affine.clicked.connect(lambda: self.canvas.setMode("AFFINE"))
        btn_perspective.clicked.connect(lambda: self.canvas.setMode("PROJECTIVE"))
        btn_reset.clicked.connect(self.canvas.reset)

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(btn_translation)
        layout.addWidget(btn_rigid)
        layout.addWidget(btn_similarity)
        layout.addWidget(btn_affine)
        layout.addWidget(btn_perspective)
        layout.addWidget(btn_reset)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.setWindowTitle("Transformation Editor")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(600, 600)
    window.show()
    sys.exit(app.exec())
```
