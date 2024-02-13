'use client'
import Image from "next/image";
import styles from "../page.module.css";


export default function Home() {
  return (
    <main className={styles.main}>
      

      <div >
        <Image
          className={styles.logo}
          src="/DELI_logo.svg"
          alt="Next.js Logo"
          width={180}
          height={37}
          priority
        />


      </div>
      <h1 className="title" >¡Bienvenido a DELI!</h1>
      <h3 className="text" >Muchas gracias por unirte a nuestra comunidad, pronto te estara llegando un mail con mas detalles</h3>
    </main>
  );
}
