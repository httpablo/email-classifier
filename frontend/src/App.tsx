import { useState } from "react";
import { Header } from "./components/Header";
import { UploadForm } from "./components/UploadForm";
import { AnalysisResult } from "./components/AnalysisResult";
import type { AnalysisResponse } from "./types";
import { Toaster } from "sonner";

function App() {
  const [result, setResult] = useState<AnalysisResponse | null>(null);

  return (
    <div className="min-h-screen bg-linear-to-br from-gray-50 to-gray-100 py-12 px-4 font-sans">
      <div className="max-w-3xl mx-auto">
        <Header />

        <main className="transition-all duration-500 ease-in-out">
          {!result ? (
            <UploadForm onSuccess={setResult} />
          ) : (
            <AnalysisResult data={result} onReset={() => setResult(null)} />
          )}
        </main>

        <footer className="mt-12 text-center text-sm text-gray-400">
          <p>Desenvolvido por @httpablo • {new Date().getFullYear()}</p>
        </footer>
      </div>
      <Toaster position="top-center" richColors />
    </div>
  );
}

export default App;
