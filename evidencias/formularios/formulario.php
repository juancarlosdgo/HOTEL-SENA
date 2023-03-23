<?php
if (isset($_post["envio"]))
{
    require_once("formulario2.php");
}
else
{
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="formulario.css">
    <title>Formulario Estudiantes</title>
</head>
<body>
    <section class="formulario_registro">
        <h2>Formulario Captura</h2>
        <form action="formulario2.php" method="post">
            <input type="text" class="controles" name="ident" 
            placeholder="Digite el numero de documento">
            <input type="text" class="controles" name="nombres" 
            placeholder="Digite los nombres">
            <input type="text" class="controles" name="Direccion" 
            placeholder="Digite la direccion">
            <input type="text" class="controles" name="Telefono"
            placeholder="Digite el numero telefonico">
            <input type="text" class="controles" name="Correo" 
            placeholder="Digite el correo">
            <br>
            <input class="botones" type="submit" name="envio" value="envio">
        </form>
    </section>
</body>
</html>

<?php
}
?>