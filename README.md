## **Project Name:** Corigine Technical Assignment

**Description:** <br>This technical assignment is part of the interview process for a position at Corigine. The program finds the factorial of the user's input, and sums the individual digits of the factorial. The project is packaged and is executable as a Docker container.

**Table of Contents:**
<ol type="i">
  <li>Installation</li>
  <li>Usage</li>
  <li>License</li>
</ol>

**1.  Installation:**<br>This project can be cloned or downloaded and it includes the following files:
<ul>
  <li>app/factorial-digits.py  -   This is the source code within the "app" folder</li>
  <li>Dockerfile               -   The file to build the Docker image</li>
  <li>dependencies.txt         -   This includes all the dependencies</li>
</ul>

**2.  Usage:**<br>To run the project you would need to follow these steps:
* Building the Docker image:
  ```
  $ docker build -t factorial-digits .
  ```          
* To run the program:
  ```
  $ docker run --rm factorial-digits [int]
  ```  
  
For testing purposes, I've run the following commands and received the corresponding outputs:
  ```
  $ docker run --rm factorial-digits 10
  >>
  27
  $ docker run --rm factorial-digits 100
  >>
  648.0
  $ docker run --rm factorial-digits 1000
  >>
  10539
  $ docker run --rm factorial-digits -5
  >>
  Invalid! Please enter a positive integer.
  $ docker run --rm factorial-digits Ten
  >>
  Error! Please enter a positive value of int() type
  ```
  
**3.  License:** MIT license

