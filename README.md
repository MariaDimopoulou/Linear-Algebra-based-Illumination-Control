# Linear-Algebra-based-Illumination-Control
This Python script implements an algorithm for optimizing lighting distribution across regions by adjusting lamp powers.

The lighting optimization problem addressed in this project was inspired by a scenario presented in the book 'Introduction to Applied Linear Algebra' from Cambridge University Press (Stephen Boyd, Lieven Vandenberghe).
The book served as a valuable resource, providing a practical application that sparked the exploration of linear algebra concepts for solving real-world problems. The problem presented in this project involves adjusting lamp powers to achieve a desired illumination pattern, showcasing the application of linear algebra techniques in the field of lighting design and optimization.

**Problem Description**
A set of n lamps illuminates an area that we divide into m regions or pixels. We let li denote the lighting level in region i, so the m-vector l gives the
illumination levels across all regions. We let pi denote the power at which lamp i operates, so the n-vector p gives the set of lamp powers. (The lamp powers are
nonnegative and also must not exceed a maximum allowed power, but we ignore these issues here.)

The matrix with the lamp position in the area is A=[[4.1,20.4,4],[14.1,21.3,3.5],[22.6,17.1,6],[5.5,12.3,4.0],[12.2,9.7,4.0],[15.3,13.8,6],[21.3,10.5,5.5],[3.9,3.3,5.0],[13.1,4.3,5.0],[20.3,4.2,4.5]].

