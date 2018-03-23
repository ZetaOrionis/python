<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Accueil</title>
  </head>
  <body>
    <ul> Liste :
      % for rep in reponse:
        % (activite, ville, complexe, cp) = rep
        <li>{{activite}}{{ville}}{{complexe}}{{cp}}</li>
      % end
    </ul>
  </body>
</html>
