import React, { useState } from 'react'
import { useRouter } from 'next/navigation'
import './styles.css';

export const RegisterForm = () => {
    const router = useRouter()
    const [formData, setFormData] = useState({
        email: '',
        fullName: '',
        age: '',
        userName: '',
        contry: ''
      });
    
      const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({ ...formData, [name]: value });
      };
    
      const handleSubmit = (e) => {
        e.preventDefault();
        console.log('Formulario enviado:', formData);
        
        setFormData({
          email: '',
          fullName: '',
          age: '',
          userName: '',
          contry: ''
        });
        router.push('registration/success')
      };
    
      const isFormValid = () => {
        return (
          formData.email !== '' &&
          formData.fullName !== '' &&
          formData.age !== '' &&
          formData.userName !== '' &&
          formData.contry !== ''
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
          <label htmlFor="contry">País:</label>
          <select id="contry" name="contry" value={formData.contry} onChange={handleChange}>
            <option value="">Selecciona un país</option>
            <option value="AR">Argentina</option>
            <option value="BR">Brasil</option>
            <option value="MX">México</option>
            
          </select>
        </div>
          <button type="submit" className='buttom' disabled={!isFormValid()}>
            Enviar
          </button>
        </form>
      );
}
