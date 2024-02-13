import React, { useState } from 'react'
import { useRouter } from 'next/navigation'
import './styles.css';
import { createUser } from '@/Presenters/Users';
import Cookies from 'js-cookie';

export const RegisterForm = () => {
  const [registerError, setregisterError] = useState(null)
    const router = useRouter()
    const [formData, setFormData] = useState({
        email: '',
        fullName: '',
        age: '',
        userName: '',
        country: ''
      });
    
      const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
      };
    
      const handleSubmit = async (e) => {
        e.preventDefault();
        console.log('Formulario enviado:', formData);
        let {mensaje, cookie} = await createUser(formData);
        if(mensaje == "OK"){
          Cookies.set('userDELI', JSON.stringify(cookie), {
            expires: 1,
            path: '/',
            domain: 'localhost',
            secure: true, 
            httpOnly: false, // Esta opcion deberia ir en true pero al estar en localhost no te permite
          });

          setFormData({
          email: '',
          fullName: '',
          age: '',
          userName: '',
          country: ''
          });
          router.push('registration/success')
        }else{
          setregisterError(mensaje)
        }
        
      };

      const isFormValid = () => {
        return (
          formData.email !== '' &&
          formData.fullName !== '' &&
          formData.age !== '' &&
          formData.userName !== '' &&
          formData.country !== ''
        );
      };
    
      return (
        <form className='form-container' onSubmit={handleSubmit}>
          <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input type="text" id="email" name="email" value={formData.email} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label htmlFor="fullName">Nombre Completo:</label>
          <input type="text" id="fullName" name="fullName" value={formData.fullName} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label htmlFor="age">Edad:</label>
          <input type="number" id="age" name="age" min="1" max="80" pattern="\d+" value={formData.age} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label htmlFor="userName">Nombre de Usuario:</label>
          <input type="text" id="userName" name="userName"  value={formData.userName} onChange={handleChange} />
        </div>
        <div className="form-group">
          <label htmlFor="country">País:</label>
          <select id="country" name="country" value={formData.country} onChange={handleChange}>
            <option value="">Selecciona un país</option>
            <option value="AR">Argentina</option>
            <option value="BR">Brasil</option>
            <option value="MX">México</option>
            
          </select>
        </div>
        {registerError&&
          <div className='errorMessage'>
            {registerError}
          </div>}
          <button type="submit" className='buttom' disabled={!isFormValid()}>
            Enviar
          </button>
        </form>
      );
}
