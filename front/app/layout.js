import { Inter } from "next/font/google";
import "./globals.css";
import styles from './layout.module.css'; 

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Bienvenido a DELI",
  description: "DELI es una plataforma que potencia tu local, agilizando ymejorando su gestión",
};

export default function RootLayout({ children }) {
  return (
    // <html lang="en">
    //   <body className={inter.className}>{children}</body>
    // </html>
    <html lang="en">
    <body className={[styles.rootLayoutBody]}>
      {children}
      <div className={styles.footer}>
        <p>© 2024 Deli. Todos los derechos reservados</p>
      </div>
    </body>
  </html>
  );
}
