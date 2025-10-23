
#Metodos de pagamento
#1. Crédito
class processar_pagamento:
   def credito(valor_final):
         print(f"Processando R${valor_final:.2f} via Cartão de Crédito...")
         # Chamada direta e acoplada a um subsistema imaginário
         if valor_final < 1000:
                print("   -> Pagamento com Credito APROVADO.")
                return True
         else:
                print("   -> Pagamento com Credito REJEITADO (limite excedido).")
                return False
#2. Pix                 
class pix(processar_pagamento):
        def pix(valor_final):
            print(f"Processando R${valor_final:.2f} via PIX...")
            print("   -> Pagamento com PIX APROVADO (QR Code gerado).")
            return True
        

#3. Debito
class debito(processar_pagamento):
        def debito(valor_final):
            print(f"Processando R${valor_final:.2f} via debito em conta...")
            print("   -> Pagamento com debito APROVADO (requer 10 segundos de espera).")
            return True  
        
#Processos de pagamentos concluidos, tem que colocar agora o desconto em pix e o frete. Colocar o __init__ para a seguranca do codigo. 