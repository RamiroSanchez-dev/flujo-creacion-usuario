'use client'
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';

import styles from "./template.module.css";
export default function Template({ children }) {
const [isLoggedIn, setIsLoggedIn] = useState(false);
const router = useRouter();

useEffect(() => {
    
}, []);



return (
    <div>
    <div className={styles.body}>
    <nav className={styles.NavTab}>
        {/* Aquí coloca tus botones de navegación */}
        <button className={styles.NavButton} onClick={() => router.push('/')}>Inicio</button>
        <button className={styles.NavButton} onClick={() => router.push('/registration')}>Registrate!</button>
        


    </nav>
    </div>
    
    <div className={styles.rootLayoutBody}>{children}</div>
    </div>
);
};
  

  