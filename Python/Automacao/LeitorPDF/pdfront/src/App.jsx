import React from "react";
import UploadPdf from "./components/UploadPdf";

function App() {
    return (
        <div>
            <h1>Buscando termos no PDF</h1>
            <h2>
                Verifique, de forma automática, 
                se uma ou mais palavras específicas
                existem no seu documento pdf
            </h2>
            <UploadPdf />
        </div>
    );
}

export default App;
