<!DOCTYPE html>
<html>
  <head>

    <title>Bambooom Diary</title>
    <meta charset="UTF-8">

  </head>
  
  <body style="background-color:black">
    <h1 style="font-family:courier; 
               font-size:250%;
               text-align:center;
               color:white
               ">Bambooom Diary</h1>
    <form action="/" method="post">
    <div align="center" style="font-family:courier;
                               font-size:150%;
                               color:white">
    吐槽: <input type="text" name="newdiary" />
    <input value="Submit" type="submit" />
    </form><br>
    <textarea rows="20" cols="50">{{diarylog}}</textarea>
    </div>
  </body>
</html>
