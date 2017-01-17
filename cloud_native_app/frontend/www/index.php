<!DOCTYPE html>
<html>
  <head>
    <title>Crêpe au sucre</title>
    <link rel="stylesheet" type="text/css" href="css/style.css">
  </head>
  <body>
    <?php include("functions.php"); ?>
    <header>
      <h1>Tombola en ligne</h1>
      <h2>Tentez votre chance !!!!</h2>
    </header>
    <main>
      <section>
        <h3>Êtes-vous authentifié ?</h3>
        <?php echo autenticate()? "Vous êtes enregistré dans la base de donnée" : "Vous n'êtes pas enregistré dans notre base de donnée. Veuillez choisir un identifiant valide." ?>
      </section>
      <?php if(autenticate()) { ?>
      <section>
        <h3>Avez-vous déjà joué ?</h3>
        <?php echo !check_played()? 'Vous avez déjà joué.' : 'Vous n\'avez pas encore joué' ?>
      </section>
      <section>
        <h3>Lien pour jouer</h3>
        <p><a href="?play=1&id=<?php echo $_GET['id'] ?>">Cliquez ici pour jouer !!</a></p>
      </section>
      <section>
        <h3>Résultat</h3>
        <?php echo !check_played() ? '<img src="images/' . get_price() . '" />':'Vous n\'avez pas encore joué' ?>
      </section>
      <?php } ?>
    </main>
  </body>
</html>

