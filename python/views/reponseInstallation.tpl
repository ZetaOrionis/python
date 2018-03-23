<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Accueil</title>
  </head>
  <body>
    <ul> Liste :
      % for rep in reponseInstallation:
        % (installationId, coordId, name, noVoie, libelleVoie, cp, commune) = rep
        <li>{{name}}{{commune}}{{cp}}{{installationId}}</li>
      % end
    </ul>
  </body>
</html>
