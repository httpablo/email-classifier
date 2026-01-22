import { CheckCircle, AlertCircle, Clock, Copy, ArrowLeft } from "lucide-react";
import { Card } from "./ui/Card";
import { Button } from "./ui/Button";
import type { AnalysisResultProps } from "../types";
import { toast } from "sonner";

export function AnalysisResult({ data, onReset }: AnalysisResultProps) {
  const isProductive = data.classification === "Produtivo";

  const getBadgeColor = () =>
    isProductive
      ? "bg-green-100 text-green-700 border-green-200"
      : "bg-orange-100 text-orange-700 border-orange-200";
  const getIcon = () =>
    isProductive ? (
      <CheckCircle className="w-5 h-5" />
    ) : (
      <AlertCircle className="w-5 h-5" />
    );

  const handleCopy = () => {
    navigator.clipboard.writeText(data.suggested_response);
    toast.success("Resposta copiada!");
  };

  return (
    <div className="space-y-6 animate-fade-in-up">
      <Card className="p-6 border-t-4 border-t-blue-500">
        <div className="flex justify-between items-start mb-6">
          <div>
            <h3 className="text-gray-500 text-sm font-medium uppercase tracking-wider">
              Classificação
            </h3>
            <div
              className={`mt-2 inline-flex items-center px-4 py-1.5 rounded-full border ${getBadgeColor()}`}
            >
              <span className="mr-2">{getIcon()}</span>
              <span className="font-bold text-lg">{data.classification}</span>
            </div>
          </div>
        </div>

        <div className="space-y-2">
          <h3 className="text-gray-500 text-sm font-medium uppercase tracking-wider flex items-center justify-between">
            <span>Sugestão de Resposta</span>
            <button
              className="text-blue-600 hover:text-blue-800 text-xs flex items-center cursor-pointer"
              onClick={handleCopy}
            >
              <Copy className="w-3 h-3 mr-1" /> Copiar
            </button>
          </h3>
          <div className="w-full min-h-40 p-4 bg-gray-50 rounded-lg border border-gray-200 text-gray-700 font-mono text-sm whitespace-pre-wrap leading-relaxed">
            {data.suggested_response}
          </div>
        </div>

        <div className="mt-6 pt-4 border-t border-gray-100 flex justify-between items-center text-xs text-gray-400">
          <span className="flex items-center">
            <Clock className="w-3 h-3 mr-1" /> Processado em {data.process_time}
            s
          </span>
        </div>
      </Card>

      <Button onClick={onReset} className="bg-gray-800 hover:bg-gray-900">
        <ArrowLeft className="w-4 h-4 mr-2" /> Analisar Outro Email
      </Button>
    </div>
  );
}
