'use client'
import Image from "next/image";
import styles from "./page.module.css";
import { RegisterForm } from "@/components/forms/RegisterForm";


export default function Home() {
  
  return (
    <main className={styles.main}>
      
      <title>Registro de usuario DELI</title>
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
      <div className="sectionFrame">
        <RegisterForm/>
      </div>
    </main>
  );
}
