import { Bot } from "lucide-react";

export function Header() {
  return (
    <header className="text-center space-y-4 mb-10">
      <div className="inline-flex items-center justify-center p-3 bg-blue-50 rounded-full mb-2">
        <Bot className="w-10 h-10 text-blue-600" />
      </div>
      <h1 className="text-4xl font-extrabold text-gray-900 tracking-tight">
        Email <span className="text-blue-600">Classifier</span>
      </h1>
      <p className="text-lg text-gray-500 max-w-2xl mx-auto">
        Triagem automática de emails utilizando Inteligência Artificial para
        otimizar o fluxo de atendimento.
      </p>
    </header>
  );
}
