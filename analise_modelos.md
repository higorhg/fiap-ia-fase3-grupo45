# Análise dos Modelos

## Melhor modelo

O melhor desempenho foi do **Naive Bayes**:

| Modelo | Accuracy | F1 macro |
|---|---:|---:|
| Naive Bayes | **0.9795** | **0.9795** |
| Random Forest | 0.9727 | 0.9726 |
| KNN | 0.9659 | 0.9659 |
| Gradient Boosting | 0.9500 | 0.9502 |
| Decision Tree | 0.9227 | 0.9218 |

Isso faz sentido porque o dataset parece ter classes bem separadas pelas variáveis agronômicas. O Naive Bayes funciona muito bem quando os padrões das classes são relativamente distintos, mesmo usando uma hipótese simples de independência entre variáveis.

## Variáveis mais importantes

Pelos modelos baseados em árvores, principalmente **Random Forest** e **Gradient Boosting**, as variáveis mais relevantes foram:

1. `humidity`
2. `rainfall`
3. `P`
4. `N`
5. `K`
6. `temperature`
7. `ph`

Ou seja, **umidade**, **chuva** e os nutrientes do solo tiveram maior peso na previsão da cultura recomendada. Isso também faz sentido no contexto agrícola, porque disponibilidade de água e composição do solo influenciam diretamente quais culturas se adaptam melhor.

## Pontos fortes e limitações

### Pontos fortes

- A abordagem é simples, rápida e fácil de comparar.
- Usa métricas adequadas para classificação multiclasse: `accuracy` e `f1_macro`.
- O `f1_macro` ajuda a avaliar o desempenho considerando todas as culturas, não apenas as mais frequentes.
- Testar vários modelos permite comparar abordagens simples, baseadas em distância e baseadas em árvores.

### Limitações

- O modelo depende da qualidade e representatividade do dataset.
- A divisão treino/teste é estática; não valida comportamento ao longo do tempo.
- Não considera sazonalidade, região, tipo de solo, histórico da lavoura ou custo de produção.
- Sensores reais podem ter ruído, falhas, leituras ausentes e variações temporais.
- Naive Bayes teve ótimo resultado, mas é menos interpretável em termos de importância direta das variáveis do que Random Forest ou Gradient Boosting.

## Melhorias com dados reais da FarmTech

Com dados reais dos sensores da FarmTech, o modelo poderia melhorar bastante porque passaria a refletir as condições reais da propriedade:

- Leituras contínuas de umidade, temperatura, pH e nutrientes.
- Dados históricos por talhão, cultura e safra.
- Detecção de variações ao longo do tempo, não apenas uma fotografia única.
- Melhor adaptação a microclimas e características locais do solo.
- Possibilidade de prever não só a cultura ideal, mas também risco, produtividade esperada e necessidade de irrigação ou correção do solo.

Em resumo: o modelo atual é um bom protótipo. Com sensores reais, ele poderia virar uma solução mais precisa, contextual e útil para decisão agrícola.
