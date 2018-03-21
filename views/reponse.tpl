<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Accueil</title>
  </head>
  <body>
    <ul> Liste :
      % for rep in reponse:
        <li>{{rep}}</li>
      % end
    </ul>
  </body>
</html>
