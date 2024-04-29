$(function(){

    $('.btnLimpiar').click(function(){
        $('.txtEmail, .txtPassword').val('');
        $('.txtEmail').focus();
    })

    $('.btnEnviar').click(function(){
        if($.trim($('.txtEmail').val())=="")
        {
            alert("Falta especificar el correo");
            $('.txtEmail').focus();
        }
        // validar que el correo tenga el formato correcto
        else if(! (/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test($.trim($('.txtEmail').val()))))
        {
            alert("El formato del correo no es correcto");
            $('.txtEmail').focus();
        }
        else if($.trim($('.txtPassword').val())=="")
        {
            alert("Falta especificar la clave");
            $('.txtPassword').focus();
        }
        // permitir que la clave contenga letras y numeros
        else if(!(/^[a-zA-Z0-9]+$/.test($.trim($('.txtPassword').val()))))
        {
            alert("El formato de la clave no es válido");
            $('.txtPassword').focus();
        }
        else
        {
            alert('Los datos enviados son: \n' + $('.txtEmail').val() + ' '
                                                + $('.txtPassword').val()
            )
        }
    })
})