from fastapi import APIRouter
import requests



def send_simple_message(user, email):
    html = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html lang="en">

<head>
  <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">

  <title>Grids Master Template</title>

  <style type="text/css">


    /* CLIENT-SPECIFIC STYLES */
    body,
    table,
    td,
    a {
      -webkit-text-size-adjust: 100%;
      -ms-text-size-adjust: 100%;
    }

    table,
    td {
      mso-table-lspace: 0pt;
      mso-table-rspace: 0pt;
    }

    img {
      -ms-interpolation-mode: bicubic;
    }

    /* RESET STYLES */
    img {
      border: 0;
      outline: none;
      text-decoration: none;
    }

    table {
      border-collapse: collapse !important;
    }

    body {
      margin: 0 !important;
      padding: 0 !important;
      width: 100% !important;
    }

    /* iOS BLUE LINKS */
    a[x-apple-data-detectors] {
      color: inherit !important;
      text-decoration: none !important;
      font-size: inherit !important;
      font-family: inherit !important;
      font-weight: inherit !important;
      line-height: inherit !important;
    }

    /* ANDROID CENTER FIX */
    div[style*="margin: 16px 0;"] {
      margin: 0 !important;
    }

    /* MEDIA QUERIES */
    @media all and (max-width:639px) {
      .wrapper {
        width: 320px !important;
        padding: 0 !important;
      }

      .container {
        width: 300px !important;
        padding: 0 !important;
      }

      .mobile {
        width: 300px !important;
        display: block !important;
        padding: 0 !important;
      }

      .img {
        width: 100% !important;
        height: auto !important;
      }
      

      *[class="mobileOff"] {
        width: 0px !important;
        display: none !important;
      }

      *[class*="mobileOn"] {
        display: block !important;
        max-height: none !important;
      }

      td,
      p {
        font-size: 125% !important;
      }
      
    }
  </style>
</head>

<body style="margin:0; padding:0; background-color:#ffffff;">

  <span style="display: block; width: 640px !important; max-width: 640px; height: 1px" class="mobileOff"></span>

  <center>
    <table width="100%" border="0" cellpadding="0" cellspacing="0" bgcolor="#ffffff">
      <tr>
        <td align="center" valign="top">



          <table width="640" cellpadding="0" cellspacing="0" border="0" class="wrapper" bgcolor="#FF5023">
            <tr>
              <td height="10" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
            <tr>
              <td align="center" valign="top">

                <table width="600" cellpadding="0" cellspacing="0" border="0" class="container">
                  <tr>
                    <td align="center" valign="top">
                      <img style="padding: 0 30px" width="80" src="{{ asset('https://deli.com.br/assets/img/deli_logo_light-1482dbe2.svg') }}" alt="Logo DELI">

                    </td>
                  </tr>
                </table>
              </td>
            </tr>
            <tr>
              <td height="10" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
          </table>

          <table width="640" cellpadding="0" cellspacing="0" border="0" class="wrapper" bgcolor="#FFFFFF">
            <tr>
              <td height="40" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
            <tr>
              <td align="center" valign="top">

                <table width="600" cellpadding="0" cellspacing="0" border="0" class="container">
                  <tr>
                    <td width="100" class="mobile" align="center" valign="top">
                      
                    </td>
                    <td width="400" class="mobile" align="center" valign="top" style=" color: #FF5023;font-weight: bold; font-size: 40px;">
                      ¡Bienvenido a deli """ + user+"""!
                    </td>
                    
                    <td width="100" class="mobile" align="center" valign="top">
                      
                    </td>
                  </tr>
                </table>

              </td>
            </tr>
            
          </table>

          <table width="640" cellpadding="0" cellspacing="0" border="0" class="wrapper" bgcolor="#FFFFFF">
            <tr>
              <td height="10" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
            <tr>
              <td align="center" valign="top">

                <table width="600" cellpadding="0" cellspacing="0" border="0" class="container">
                  <tr>
                    <td width="100" class="mobile" align="center" valign="top">
                      
                    </td>
                    <td width="400" class="mobile" align="center" valign="top" style="font-size: 18px;">
                      Muchas Gracias por unirte a nuestra comunidad
                    </td>
                    <td width="100" class="mobile" align="center" valign="top">
                    </td>
                  </tr>
                </table>

              </td>
            </tr>
            <tr>
              <td height="10" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
          </table>
          <table width="640" cellpadding="0" cellspacing="0" border="0" class="wrapper" bgcolor="#FFFFFF">
            <tr>
              <td height="30" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
            <tr>
              <td align="center" valign="top">

                <table width="600" cellpadding="0" cellspacing="0" border="0" class="container">
                  <tr>
                    <td width="100" class="mobile" align="center" valign="top">
                      
                    </td>
                    <td width="400" class="mobile" align="center" valign="top">
                      <img style="padding: 0 5px" width="10" src="https://deli.com.br/assets/img/icons/arrow-723b3d16.svg" alt="flecha DELI">
                      Haz click en el siguiente botón para confirmar tu registro:
                    </td>
                    
                    <td width="100" class="mobile" align="center" valign="top">
                      
                    </td>
                  </tr>
                </table>

              </td>
            </tr>
            <tr>
              <td height="30" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
          </table>
          <table width="640" cellpadding="0" cellspacing="0" border="0" class="wrapper" bgcolor="#FFFFFF">
            <tr>
              <td height="10" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
            <tr>
              <td align="center" valign="top">

                <table width="600" cellpadding="0" cellspacing="0" border="0" class="container">
                  <tr>
                    <td width="200" class="mobile" align="center" valign="top">
                      
                    </td>
                    
                    <td width="200" class="mobile" align="center" valign="top"  style="border-radius: 5px; background-color: #FF5023;padding:10px 0; color:white">
                     <a style="text-decoration: none; color: white;" href="https://deli.com.br/pt-br/" target="_blank">INGRESAR</a>
                    </td>
                    <td width="200" class="mobile" align="center" valign="top">
                      
                    </td>
                  </tr>
                </table>

              </td>
            </tr>
            <tr>
              <td height="10" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
          </table>

          
          <table width="640" cellpadding="0" cellspacing="0" border="0" class="wrapper" bgcolor="#FFFFFF">
            <tr>
              <td height="40" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
            <tr>
              <td align="center" valign="top">

                <table width="600" cellpadding="0" cellspacing="0" border="0" class="container">
                  <tr>
                    <td width="100" class="mobile" align="center" valign="top">
                      
                    </td>
                    <td width="400" class="mobile" align="center" valign="top" style="font-weight: bold;">
                      ¡Esperemos que lo disfrutes tanto como nosotros!
                    </td>
                    
                    <td width="100" class="mobile" align="center" valign="top">
                      
                    </td>
                  </tr>
                </table>

              </td>
            </tr>
            <tr>
              <td height="40" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
          </table>
          <table width="640" cellpadding="0" cellspacing="0" border="0" class="wrapper" bgcolor="#F5F5F5">
            <tr>
              <td height="30" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
            <tr>
              <td align="center" valign="top">
                <table width="600" cellpadding="0" cellspacing="0" border="0" class="container">
                  <tr>
                    <td width="120" class="mobile" align="left" valign="top">
                      <img style="padding: 0 0px" width="80" src="https://deli.com.br/assets/img/deli_logo_color-666b50b0.svg" alt="Logo DELI">
                    </td>
                    <td width="480" class="mobile" align="left" valign="top">
                      
                    </td>
                    
                  </tr>
                </table>
              </td>
            </tr>
            <tr>
              <td height="10" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
          </table>
          <table width="640" cellpadding="0" cellspacing="0" border="0" class="wrapper" bgcolor="#F5F5F5">
            
            <tr>
              <td align="center" valign="top">
                
                
                <table width="600" cellpadding="0" cellspacing="0" border="0" class="container">
                  <tr>
                    <td width="500" class="mobile footer" align="left" valign="top" style="font-size: 10px; color: #AAB1C1;">
                      Si necesitas ayuda no dudes en dirigirte a nuestra área de soporte o contactarnos a través del <strong>chat del sistemas.</strong>
                    </td>
                    <td width="100" class="mobile" align="center" valign="top">
                      
                    </td>
                    
                  </tr>
                </table>

              </td>
            </tr>
            <tr>
              <td height="40" style="font-size:10px; line-height:10px;">&nbsp;</td>
            </tr>
          </table>

        </td>
      </tr>
    </table>
  </center>
</body>

</html>

"""
    #aca deberia mandarse el mail a email pero la version de la API no permite mandar a cualquiera, solo a autorizados
    result = requests.post(
        "https://api.mailgun.net/v3/sandbox43549ae5b4d043d3a9765dd16698cf05.mailgun.org/messages",
        auth=("api", "380451a6c861f15ccd0e44ba351c462e-8c8e5529-5e33c47a"),
        data={
            "from": "Excited User <mailgun@sandbox43549ae5b4d043d3a9765dd16698cf05.mailgun.org>",
            "to": ["rsanchez@fi.uba.ar"],
            "subject": "Bienvenido a DELI",
            "html": html
        }
    )
    