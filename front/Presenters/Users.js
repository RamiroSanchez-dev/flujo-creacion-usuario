import AppConstants from "@/Constants/AppConstants";
import axios from "axios";

export async function createUser(newUser){
    
  
    const requiredFields = ['age', 'country', 'email', 'fullName', 'userName'];
    for (const field of requiredFields) {
        if (!(field in newUser)) {
            console.log(field)
          return "Faltan completar campos obligatorios"; 
        }
      }

      const headers = {
        Authorization: `Bearer ${AppConstants.ACCESS_TOKEN}`,
        'Content-Type': 'application/json',
      };
     
        let mensaje = "Ocurrió un error, pruebe mas tarde"
        let cookie;
        const response = await axios.post(`${AppConstants.API_URL}/accounts/`, newUser, { headers })
        .then(function (response) {
            console.log(response,newUser.userName,response.data.session_token);
            cookie= {'name':newUser.userName, 'token': response.data.session_token}
            mensaje ="OK"

          })
        .catch(function (error) {
            if(error.response.status == 400){
                mensaje = error.response.data.detail
            }
            console.log( "Error",error);
          });
        console.log('Respuesta', mensaje);
        console.log('cookie', cookie);
        return {mensaje,cookie};
      

}