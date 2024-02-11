'use client'
import Image from "next/image";
import styles from "./page.module.css";
import GlobalStyles from "./globals.css";
import Link from "next/link";

export default function Home() {
  return (
    <main className={styles.main}>
      

      <div className={[styles.center]}>
        <Image
          className={styles.logo}
          src="/DELI_logo.svg"
          alt="Next.js Logo"
          width={180}
          height={37}
          priority
        />

        
      </div>
      <div >
        <h1 className="title" >Bienvenido a DELI, una herramienta que va a lelvar tu negocio al proximo nivel</h1>
        <div className={[styles.center]}>
        <Link className="buttom" style={{fontSize:'20px'}} href="/registration">Empieza a usarla ya!</Link>

        </div>
      </div>

    </main>
  );
}
