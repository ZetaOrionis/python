<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Home</title>
    <meta charset="utf-8">
    <script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1/jquery.min.js"></script>
    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/themes/smoothness/jquery-ui.css" />
    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.3/jquery-ui.min.js"></script>
    <script type="text/javascript" src="{{ url('static', path='script/codeVilleComplete.js') }}" charset="utf-8"></script>
  </head>
  <body>
    <form method="get" action="/traitement">
      <p>Ville :
        <input id="ville" type="text" name="ville">
      </p>
      <p>Activité :
        <input id="activite" type="text" name="activite">
      </p>
      <input type="submit" value="Rechercher">
    </form>
  </body>
</html>
