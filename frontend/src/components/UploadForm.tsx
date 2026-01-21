import { useState, useRef, type DragEvent } from "react";
import { Upload, FileText, X, Send } from "lucide-react";
import { analyzeEmail } from "../services/api";
import { Button } from "./ui/Button";
import { Card } from "./ui/Card";
import type { AnalysisResponse } from "../types";

interface UploadFormProps {
  onSuccess: (data: AnalysisResponse) => void;
}

export function UploadForm({ onSuccess }: UploadFormProps) {
  const [file, setFile] = useState<File | null>(null);
  const [text, setText] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const validateFile = (file: File) => {
    if (!["application/pdf", "text/plain"].includes(file.type))
      return "Formato inválido. Use PDF ou TXT.";
  };

  const handleFileSelect = (selectedFile: File) => {
    const err = validateFile(selectedFile);
    if (err) {
      setError(err);
      return;
    }
    setFile(selectedFile);
    setText("");
    setError(null);
  };

  const handleDrop = (e: DragEvent) => {
    e.preventDefault();
    if (e.dataTransfer.files?.[0]) handleFileSelect(e.dataTransfer.files[0]);
  };

  const handleSubmit = async () => {
    if (!file && !text) return setError("Insira um texto ou arquivo.");

    setIsLoading(true);
    setError(null);
    const formData = new FormData();
    if (file) {
      formData.append("file", file);
    } else {
      formData.append("text_input", text);
    }

    try {
      const data = await analyzeEmail(formData);
      onSuccess(data);
    } catch {
      setError("Erro ao conectar com o servidor. Tente novamente.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <Card className="p-1">
      <div className="flex border-b border-gray-100 bg-gray-50/50">
        <button
          onClick={() => setFile(null)}
          className={`flex-1 py-3 text-sm font-medium transition-colors ${!file ? "bg-white text-blue-600 border-t-2 border-blue-600 shadow-sm" : "text-gray-500 hover:text-gray-700"}`}
        >
          Texto
        </button>
        <button
          onClick={() => setText("")}
          className={`flex-1 py-3 text-sm font-medium transition-colors ${file ? "bg-white text-blue-600 border-t-2 border-blue-600 shadow-sm" : "text-gray-500 hover:text-gray-700"}`}
        >
          Arquivo
        </button>
      </div>

      <div className="p-6 space-y-6">
        {!file ? (
          <textarea
            className="w-full h-48 p-4 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent resize-none transition-all placeholder:text-gray-300"
            placeholder="Cole o conteúdo do email aqui..."
            value={text}
            onChange={(e) => setText(e.target.value)}
            disabled={isLoading}
          />
        ) : (
          <div className="flex items-center justify-between p-4 bg-blue-50 border border-blue-100 rounded-lg animate-in fade-in zoom-in-95">
            <div className="flex items-center space-x-4">
              <div className="p-2 bg-white rounded-lg shadow-sm">
                <FileText className="w-6 h-6 text-blue-600" />
              </div>
              <div className="overflow-hidden">
                <p className="font-medium text-gray-900 truncate max-w-50 sm:max-w-xs">
                  {file.name}
                </p>
                <p className="text-xs text-gray-500">
                  {(file.size / 1024).toFixed(2)} KB
                </p>
              </div>
            </div>
            <button
              onClick={() => setFile(null)}
              className="text-gray-400 hover:text-red-500"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        )}

        {!file && !text && (
          <div
            onDragOver={(e) => e.preventDefault()}
            onDrop={handleDrop}
            onClick={() => fileInputRef.current?.click()}
            className="border-2 border-dashed border-gray-300 rounded-lg p-8 flex flex-col items-center justify-center text-gray-400 hover:border-blue-400 hover:bg-blue-50/50 cursor-pointer transition-all"
          >
            <Upload className="w-10 h-10 mb-3 text-gray-300" />
            <p className="text-sm">
              Arraste seu arquivo .pdf/.txt ou clique aqui
            </p>
            <input
              type="file"
              className="hidden"
              ref={fileInputRef}
              accept=".pdf,.txt"
              onChange={(e) =>
                e.target.files?.[0] && handleFileSelect(e.target.files[0])
              }
            />
          </div>
        )}

        {error && (
          <div className="p-3 text-sm text-red-600 bg-red-50 rounded-md border border-red-100 text-center">
            {error}
          </div>
        )}

        <Button
          onClick={handleSubmit}
          isLoading={isLoading}
          disabled={!file && !text}
        >
          <Send className="w-4 h-4 mr-2" /> Analisar Email
        </Button>
      </div>
    </Card>
  );
}
