import { Inter } from "next/font/google";
import "./globals.css";
import styles from './layout.module.css'; 

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Registro DELI",
  description: "Pagina de registro de DELI",
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
        <p>Hola, soy el footer</p>
      </div>
    </body>
  </html>
  );
}
