export interface AnalysisResponse {
  original_text: string;
  cleaned_text: string;
  classification: "Produtivo" | "Improdutivo";
  confidence: number;
  suggested_response: string;
  process_time: number;
}

export interface AnalysisResultProps {
  data: AnalysisResponse;
  onReset: () => void;
}
