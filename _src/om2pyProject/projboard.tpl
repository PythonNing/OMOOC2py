<!DOCTYPE html>
<html>
  <head>

    <title>Project Board for OMOOC2py</title>
    <meta charset="UTF-8">
    <style>
    h1 {
      color: #2F4F4F;
      font-family: courier;
      font-size: 280%;
      text-align: center;
    }
    h3 {
      color:white;
      font-family: Georgia;
      text-align: center;
    }
    div {
      color: #F92672;
      font-family: courier;
      font-size: 120%;
    }
    div.info {
      color: #E6DB74 
    }
    div.readlog {
      color: #1E90FF;
      font-family: Georgia;
      text-align: center;
    }
    i.etime {color: #A6E22E; font-size: 100%}
    pre.comment {color:#E6DB74; font-size: 120%}
    </style>

  </head>
  
  <body style="background-color:black">
    <h1>Project Board for OMOOC2py</h1>
    <h3>Give comments to the teams!</h3>
    
    <div class=info align="center">
      <table border="0" cellpadding="2" width="600px">
        <tr>
          <td colspan="2">带它回家 Stray Pets Helper</td>
        </tr>
        <tr>
          <td width="200px">@xpgeng</td>
          <td rowspan="3">流浪宠物信息平台</td>
        </tr>
        <tr>
          <td>@huijuannan</td>
        </tr>
        <tr>
          <td>@tiezipy</td>
        </tr>
      </table>
    </div>
    <br><br>
    <form action="/" method="post">
    <div align="center">
    给他们留个言吧~ <br>
    <input type="text" name="newcomment" size="30"/><br> 
    <input value="Submit" type="submit"/>
    </div>
    </form><br>
    
    %for i in comment_log:
      <div class=readlog>
        <i class=etime>{{i['time']}}</i>
        <pre class=comment>{{i['comment']}}</pre>
      </div>
    %end
  </body>
</html>

