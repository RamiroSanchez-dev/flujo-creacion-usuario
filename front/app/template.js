'use client'
import React, { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import styles from "./template.module.css";
import Cookies from 'js-cookie';

export default function Template({ children }) {
    const [userLogged, setUserLogged] = useState(false)
    const router = useRouter();

    useEffect(() => {
        const cookieValue = Cookies.get('userDELI');
        console.log(cookieValue)
        setUserLogged(JSON.parse(cookieValue))
    }, []);

    return (
    <div>
        <div className={styles.body}>
        <nav className={styles.NavTab}>
            <button className={styles.NavButton} onClick={() => router.push('/')}>Inicio</button>
            {
                userLogged?
                <div className={styles.userName}>
                    ¡Hola, {userLogged.name}!
                </div>
                :
                <button className={styles.NavButton} onClick={() => router.push('/registration')}>Registrate!</button>
            }
        </nav>
        </div>
        <div className={styles.rootLayoutBody}>{children}</div>
    </div>
    );
};
  

  