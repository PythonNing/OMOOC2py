<!DOCTYPE html>
<html>
  <head>

    <title>Bambooom Diary</title>
    <meta charset="UTF-8">
    <style>
    h1 {
      color: white;
      font-family: courier;
      font-size: 260%;
      text-align: center;
    }
    h3 {
      color:white;
      font-family: courier;
      text-align: center;
    }
    div {
      color: white;
      font-family: courier;
      font-size: 120%;
    }
    </style>

  </head>
  
  <body style="background-color:black">
    <h1>Bambooom Diary</h1>
    <h3>All those moments will be lost in time,<br>
      like tears in rain.<br>
      Time to write.</h3>
    <form action="/" method="post">

    <div align="center">
    吐槽: <input type="text" name="newdiary" size="30"/><br>
    标签: <input type="text" name="tags" size="30"/><br> 
    <input value="Submit" type="submit"/>
    </form><br><br>
    <textarea rows="20" cols="50">{{diarylog}}</textarea>
    </div>

  </body>
</html>

