# Python_Patterns_Tutorial
<h2>How to draw patterns with Python code</h2>
<p>There are 5 main patterns in Python, which can be used as building blocks for almost any pattern. They are:</p>
<ul>
  <li>square</li>
  <li>increasing triangle</li>
  <li>decreasing triangle</li>
  <li>increasing right triangle</li>
  <li>decreasing right triangle</li>
</ul>
<p>All the code is included in the repository.</p>
<h3>Square</h3>
<p>The square is the simplest pattern, but its code can be used as a foundation to all the other patterns.</p>
<img align="right" width="129" height="129" src="https://i.imgur.com/LJ4Zkgx.png">

```python
n = 5
for i in range(n):
    for k in range(n):
        print("*", end=" ")
    print()
```

<h3>Increasing triangle</h3>
<p>By changing the nested loop's range to <strong>(i + 1)</strong> we now make it iterate from 1 to 5 times not just 5.</p>
<img align="right" width="129" height="129" src="https://i.imgur.com/CPdplBd.png">

```python
n = 5
for i in range(n):
    for k in range(i + 1):
        print("*", end=" ")
    print()
```
<h3>Decreasing triangle</h3>
<p>By changing the nested loop's range to <strong>(i, n)</strong> we now make it iterate from 0 to 5 on the first iteration, but <strong>i</strong> keeps increasing so we print less stars each iteration.</p>
<img align="right" width="129" height"129" src="https://i.imgur.com/nJDU0DO.png">

```python
n = 5
for i in range(n):
    for k in range(i, n):
        print("*", end=" ")
    print()
```
<h3>Increasing right triangle</h3>
<p>In order to print a triangle on the right, we first have to print blank spaces. To do that, we just copy the decreasing triangle loop and replace the <strong>'*'</strong> with a blank space. After that bellow it, we paste the increasing triangle loop.</p>
<img align="right" width="129" height"129" src="https://i.imgur.com/as0xFIx.png">

```python
n = 5
for i in range(n):
    for k in range(i, n):
        print(" ", end=" ")
    for j in range(i + 1):
        print("*", end=" ")
    print()
```
<h3>Decreasing right triangle</h3>
<p>The decreasing right triangle is almost the same, we just flip around the loop ranges of <strong>k</strong> and <strong>j</strong>.</p>
<img align="right" width="129" height"129" src="https://i.imgur.com/ocdg3Dc.png">

```python
for i in range(n):
    for k in range(i + 1):
        print(" ", end=" ")
    for j in range(i, n):
        print("*", end=" ")
    print()
```

<h4 align="center">Thank you for reading. Now with all these basic shapes you can create more complicated ones by putting them together.</h4>
<h4 align="center"><a href="https://replit.com/@MarkDelchev/patterns#main.py">Click here to test the code.</a></h4>
