This is the result of the command `./run @mode=simple -Parser.verbose 5 -Parser.visualizeChartFilling true -Grammar.inPaths data/tutorial-arithmetic.grammar -FeatureExtractor.featureDomains rule -Dataset.inPaths train:data/tutorial-arithmetic.examples -Learner.maxTrainIters 3`.
```
main() {
  Grammar.read {
    15 rules
  }
  Parser: 4 catUnaryRules (sorted), 11 nonCatUnaryRules (in trie)
  Dataset.read {
    Reading data/tutorial-arithmetic.examples {
      Example data/tutorial-arithmetic.examples:0 (0): [three, and, four] => (number 7)
    }
  }
  Learner.learn() {
    Iteration 0/3 {
      Processing iter=0.train: 1 examples {
        Examples {
          iter=0.train: example 0/1: data/tutorial-arithmetic.examples:0 {
            Example: three and four {
              Tokens: [three, and, four]
              Lemmatized tokens: [three, and, four]
              POS tags: [CD, UNK, CD]
              NER tags: [NUMBER, UNK, NUMBER]
              NER values: [3, UNK, 4]
              targetValue: (number 7)
              Dependency children: []
            }
            Parser.parse: parse {
              ParserState.infer {
                featurizeAndScoreDerivation(score=0) $TOKEN 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $TOKEN 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $TOKEN 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:2[three and]: (derivation (formula (string "three and")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "three and")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:2[three and]: (derivation (formula (string "three and")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "three and")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:3[three and four]: (derivation (formula (string "three and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "three and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:3[three and four]: (derivation (formula (string "three and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "three and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 1:3[and four]: (derivation (formula (string "and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 1:3[and four]: (derivation (formula (string "and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string four)) (type fb:type.text))
                applyNonCatUnaryRules(start=0, end=1, i=0, children=[], 0 rules)
                applyCatUnaryRules 0 1 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string three)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:1): 1 derivations {
                  $PHRASE(0,1): (string three) three, [score=0.0]
                }
                applyRule 0 1 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string three)) (type fb:type.text))]
                featurizeAndScoreDerivation(score=0) $Expr 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Expr -> $PHRASE (NumberFn)]
                addToChart $Expr: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Expr:0:1): 1 derivations {
                  $Expr(0,1): (number 3) , [score=0.0]
                }
                applyRule 0 1 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $Intermediate2 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate2:0:1): 1 derivations {
                  $Intermediate2(0,1): (number 3) , [score=0.0]
                }
                applyRule 0 1 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $Intermediate3 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate3:0:1): 1 derivations {
                  $Intermediate3(0,1): (number 3) , [score=0.0]
                }
                applyRule 0 1 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $ROOT 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (number 3)) (type fb:type.int))
                ParserState.pruneCell($LEMMA_PHRASE:0:1): 1 derivations {
                  $LEMMA_PHRASE(0,1): (string three) three, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:0:1): 1 derivations {
                  $TOKEN(0,1): (string three) three, [score=0.0]
                }
                ParserState.pruneCell($ROOT:0:1): 1 derivations {
                  $ROOT(0,1): (number 3) , [score=0.0]
                }
                ParserState.pruneCell($LEMMA_TOKEN:0:1): 1 derivations {
                  $LEMMA_TOKEN(0,1): (string three) three, [score=0.0]
                }
                applyNonCatUnaryRules(start=1, end=2, i=1, children=[], 0 rules)
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[], 2 rules)
                applyRule 1 2 $Operator -> and (ConstantFn (lambda y (lambda x (call * (var x) (var y))))) []
                featurizeAndScoreDerivation(score=0) $Operator 1:2[and]: (derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))) [rule: $Operator -> and (ConstantFn (lambda y (lambda x (call * (var x) (var y)))))]
                addToChart $Operator: (derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))
                applyRule 1 2 $Operator -> and (ConstantFn (lambda y (lambda x (call + (var x) (var y))))) []
                featurizeAndScoreDerivation(score=0) $Operator 1:2[and]: (derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))) [rule: $Operator -> and (ConstantFn (lambda y (lambda x (call + (var x) (var y)))))]
                addToChart $Operator: (derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyCatUnaryRules 1 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string and)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:1:2): 1 derivations {
                  $PHRASE(1,2): (string and) and, [score=0.0]
                }
                applyRule 1 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string and)) (type fb:type.text))]
                applyCatUnaryRules 1 2 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 1 2 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 1 2 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($LEMMA_PHRASE:1:2): 1 derivations {
                  $LEMMA_PHRASE(1,2): (string and) and, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:1:2): 1 derivations {
                  $TOKEN(1,2): (string and) and, [score=0.0]
                }
                ParserState.pruneCell($Operator:1:2): 2 derivations {
                  $Operator(1,2): (lambda y (lambda x (call * (var x) (var y)))) , [score=0.0]
                  $Operator(1,2): (lambda y (lambda x (call + (var x) (var y)))) , [score=0.0]
                }
                ParserState.pruneCell($LEMMA_TOKEN:1:2): 1 derivations {
                  $LEMMA_TOKEN(1,2): (string and) and, [score=0.0]
                }
                applyNonCatUnaryRules(start=2, end=3, i=2, children=[], 0 rules)
                applyCatUnaryRules 2 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string four)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:2:3): 1 derivations {
                  $PHRASE(2,3): (string four) four, [score=0.0]
                }
                applyRule 2 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string four)) (type fb:type.text))]
                featurizeAndScoreDerivation(score=0) $Expr 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Expr -> $PHRASE (NumberFn)]
                addToChart $Expr: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Expr:2:3): 1 derivations {
                  $Expr(2,3): (number 4) , [score=0.0]
                }
                applyRule 2 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $Intermediate2 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate2:2:3): 1 derivations {
                  $Intermediate2(2,3): (number 4) , [score=0.0]
                }
                applyRule 2 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $Intermediate3 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate3:2:3): 1 derivations {
                  $Intermediate3(2,3): (number 4) , [score=0.0]
                }
                applyRule 2 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $ROOT 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (number 4)) (type fb:type.int))
                ParserState.pruneCell($LEMMA_PHRASE:2:3): 1 derivations {
                  $LEMMA_PHRASE(2,3): (string four) four, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:2:3): 1 derivations {
                  $TOKEN(2,3): (string four) four, [score=0.0]
                }
                ParserState.pruneCell($ROOT:2:3): 1 derivations {
                  $ROOT(2,3): (number 4) , [score=0.0]
                }
                ParserState.pruneCell($LEMMA_TOKEN:2:3): 1 derivations {
                  $LEMMA_TOKEN(2,3): (string four) four, [score=0.0]
                }
                applyNonCatUnaryRules(start=0, end=2, i=0, children=[], 0 rules)
                applyNonCatUnaryRules(start=0, end=2, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=2, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyCatUnaryRules 0 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:2): 1 derivations {
                  $PHRASE(0,2): (string "three and") three and, [score=0.0]
                }
                applyRule 0 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and")) (type fb:type.text))]
                applyCatUnaryRules 0 2 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 0 2 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 0 2 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($LEMMA_PHRASE:0:2): 1 derivations {
                  $LEMMA_PHRASE(0,2): (string "three and") three and, [score=0.0]
                }
                applyNonCatUnaryRules(start=1, end=3, i=1, children=[], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[], 2 rules)
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=3, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))], 1 rules)
                applyRule 1 3 $Partial -> $Operator $Expr (JoinFn forward) [(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $Partial 1:3[and four]: (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any))) [rule: $Partial -> $Operator $Expr (JoinFn forward)]
                addToChart $Partial: (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=3, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))], 1 rules)
                applyRule 1 3 $Partial -> $Operator $Expr (JoinFn forward) [(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $Partial 1:3[and four]: (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any))) [rule: $Partial -> $Operator $Expr (JoinFn forward)]
                addToChart $Partial: (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))
                applyCatUnaryRules 1 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "and four")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:1:3): 1 derivations {
                  $PHRASE(1,3): (string "and four") and four, [score=0.0]
                }
                applyRule 1 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "and four")) (type fb:type.text))]
                applyCatUnaryRules 1 3 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 1 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 1 3 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($Partial:1:3): 2 derivations {
                  $Partial(1,3): ((lambda y (lambda x (call * (var x) (var y)))) (number 4)) , [score=0.0]
                  $Partial(1,3): ((lambda y (lambda x (call + (var x) (var y)))) (number 4)) , [score=0.0]
                }
                ParserState.pruneCell($LEMMA_PHRASE:1:3): 1 derivations {
                  $LEMMA_PHRASE(1,3): (string "and four") and four, [score=0.0]
                }
                applyNonCatUnaryRules(start=0, end=3, i=0, children=[], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))], 1 rules)
                applyRule 0 3 $Expr -> $Expr $Partial (JoinFn backward) [(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))]
                featurizeAndScoreDerivation(score=0) $Expr 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Expr -> $Expr $Partial (JoinFn backward)]
                addToChart $Expr: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))], 1 rules)
                applyRule 0 3 $Expr -> $Expr $Partial (JoinFn backward) [(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))]
                featurizeAndScoreDerivation(score=0) $Expr 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Expr -> $Expr $Partial (JoinFn backward)]
                addToChart $Expr: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))], 0 rules)
                applyCatUnaryRules 0 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and four")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:3): 1 derivations {
                  $PHRASE(0,3): (string "three and four") three and four, [score=0.0]
                }
                applyRule 0 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and four")) (type fb:type.text))]
                applyCatUnaryRules 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Expr:0:3): 2 derivations {
                  $Expr(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=0.0]
                  $Expr(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=0.0]
                }
                applyRule 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=0) $Intermediate2 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=0) $Intermediate2 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyCatUnaryRules 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Intermediate2:0:3): 2 derivations {
                  $Intermediate2(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=0.0]
                  $Intermediate2(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=0.0]
                }
                applyRule 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=0) $Intermediate3 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=0) $Intermediate3 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyCatUnaryRules 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Intermediate3:0:3): 2 derivations {
                  $Intermediate3(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=0.0]
                  $Intermediate3(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=0.0]
                }
                applyRule 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=0) $ROOT 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=0) $ROOT 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                ParserState.pruneCell($LEMMA_PHRASE:0:3): 1 derivations {
                  $LEMMA_PHRASE(0,3): (string "three and four") three and four, [score=0.0]
                }
                ParserState.pruneCell($ROOT:0:3): 2 derivations {
                  $ROOT(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=0.0]
                  $ROOT(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=0.0]
                }
              }
              Parser.ensureExecuted 
            }
            Parser.setEvaluation: 2 candidates {
              TopTrue (1) - Pred (0) = Diff features [sum = 0] (format is feature value * weight) {
                [ rule :: $Operator -> and (ConstantFn (lambda y (lambda x (call * (var x) (var y))))) ]      0 = -1 * 0
                [ rule :: $Operator -> and (ConstantFn (lambda y (lambda x (call + (var x) (var y))))) ]      0 = 1 * 0
              }
              TopTrue (1) - Pred (0) = Diff choices 
              True@0001: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (value (number 7)) (type fb:type.any)) [score=0, prob=0.500, comp=1]
              Pred@0000: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (value (number 12)) (type fb:type.any)) [score=0, prob=0.500, comp=0]
              Pred@0001: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (value (number 7)) (type fb:type.any)) [score=0, prob=0.500, comp=1]
            }
            Updating learner weights {
              L2 norm: 0.7071067811865476
            }
            Current: correct=0.500 oracle=1 partCorrect=0.500 partOracle=1 correctIndexAfterParse=1 correctMaxBeamPosition=1 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=90 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
            Cumulative(iter=0.train): correct=0.500 oracle=1 partCorrect=0.500 partOracle=1 correctIndexAfterParse=1 correctMaxBeamPosition=1 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=90 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
          }
        }
        Stats for iter=0.train: correct=0.500 oracle=1 partCorrect=0.500 partOracle=1 correctIndexAfterParse=1 correctMaxBeamPosition=1 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=90 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
        Evaluation stats for iter=0.train {
          correct = 0.500/ << 0.500 ~ 0 >> /0.500 (1)
          oracle = 1/ << 1 ~ 0 >> /1 (1)
          partCorrect = 0.500/ << 0.500 ~ 0 >> /0.500 (1)
          partOracle = 1/ << 1 ~ 0 >> /1 (1)
          correctIndexAfterParse = 1/ << 1 ~ 0 >> /1 (1)
          correctMaxBeamPosition = 1/ << 1 ~ 0 >> /1 (1)
          correctMaxUnsortedBeamPosition = 1/ << 1 ~ 0 >> /1 (1)
          parsed = 1/ << 1 ~ 0 >> /1 (1)
          numCandidates = 2/ << 2 ~ 0 >> /2 (1)
          parsedNumCandidates = 2/ << 2 ~ 0 >> /2 (1)
          numTokens = 3/ << 3 ~ 0 >> /3 (1)
          parseTime = 90/ << 90 ~ 0 >> /90 (1)
          maxCellSize = 2@$Operator:1:2/ << 2 ~ 0 >> /2@$Operator:1:2 (1)
          fallOffBeam = 0/ << 0 ~ 0 >> /0 (1)
          totalDerivs = 38/ << 38 ~ 0 >> /38 (1)
          numOfFeaturizedDerivs = 38/ << 38 ~ 0 >> /38 (1)
        }
      }
      StopWatchSet {
        FeatureExtractor.extractLocal	0.001s (0.0s x 38)
        NumberFn	0.011s (0.001s x 6)
        SelectFn	0.001s (0.0s x 8)
        IdentityFn	0.0s (0.0s x 4)
        ConstantFn	0.0s (0.0s x 2)
        JoinFn	0.002s (0.0s x 4)
        Executor.execute	0.003s (0.001s x 2)
        Parser.parse	0.094s (0.094s x 1)
        Learner.updateWeights	0.0s (0.0s x 1)
      }
      StopWatchSet {
        FeatureExtractor.extractLocal	0.001s (0.0s x 38)
        NumberFn	0.011s (0.001s x 6)
        SelectFn	0.001s (0.0s x 8)
        IdentityFn	0.0s (0.0s x 4)
        ConstantFn	0.0s (0.0s x 2)
        JoinFn	0.002s (0.0s x 4)
        Executor.execute	0.003s (0.001s x 2)
        Parser.parse	0.094s (0.094s x 1)
        Learner.updateWeights	0.0s (0.0s x 1)
      }
    }
    Iteration 1/3 {
      Processing iter=1.train: 1 examples {
        Examples {
          iter=1.train: example 0/1: data/tutorial-arithmetic.examples:0 {
            Example: three and four {
              Tokens: [three, and, four]
              Lemmatized tokens: [three, and, four]
              POS tags: [CD, UNK, CD]
              NER tags: [NUMBER, UNK, NUMBER]
              NER values: [3, UNK, 4]
              targetValue: (number 7)
              Dependency children: []
            }
            Parser.parse: parse {
              ParserState.infer {
                featurizeAndScoreDerivation(score=0) $TOKEN 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $TOKEN 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $TOKEN 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:2[three and]: (derivation (formula (string "three and")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "three and")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:2[three and]: (derivation (formula (string "three and")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "three and")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:3[three and four]: (derivation (formula (string "three and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "three and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:3[three and four]: (derivation (formula (string "three and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "three and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 1:3[and four]: (derivation (formula (string "and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 1:3[and four]: (derivation (formula (string "and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string four)) (type fb:type.text))
                applyNonCatUnaryRules(start=0, end=1, i=0, children=[], 0 rules)
                applyCatUnaryRules 0 1 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string three)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:1): 1 derivations {
                  $PHRASE(0,1): (string three) three, [score=0.0]
                }
                applyRule 0 1 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string three)) (type fb:type.text))]
                featurizeAndScoreDerivation(score=0) $Expr 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Expr -> $PHRASE (NumberFn)]
                addToChart $Expr: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Expr:0:1): 1 derivations {
                  $Expr(0,1): (number 3) , [score=0.0]
                }
                applyRule 0 1 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $Intermediate2 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate2:0:1): 1 derivations {
                  $Intermediate2(0,1): (number 3) , [score=0.0]
                }
                applyRule 0 1 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $Intermediate3 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate3:0:1): 1 derivations {
                  $Intermediate3(0,1): (number 3) , [score=0.0]
                }
                applyRule 0 1 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $ROOT 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (number 3)) (type fb:type.int))
                ParserState.pruneCell($LEMMA_PHRASE:0:1): 1 derivations {
                  $LEMMA_PHRASE(0,1): (string three) three, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:0:1): 1 derivations {
                  $TOKEN(0,1): (string three) three, [score=0.0]
                }
                ParserState.pruneCell($ROOT:0:1): 1 derivations {
                  $ROOT(0,1): (number 3) , [score=0.0]
                }
                ParserState.pruneCell($LEMMA_TOKEN:0:1): 1 derivations {
                  $LEMMA_TOKEN(0,1): (string three) three, [score=0.0]
                }
                applyNonCatUnaryRules(start=1, end=2, i=1, children=[], 0 rules)
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[], 2 rules)
                applyRule 1 2 $Operator -> and (ConstantFn (lambda y (lambda x (call * (var x) (var y))))) []
                featurizeAndScoreDerivation(score=-1) $Operator 1:2[and]: (derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))) [rule: $Operator -> and (ConstantFn (lambda y (lambda x (call * (var x) (var y)))))]
                addToChart $Operator: (derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))
                applyRule 1 2 $Operator -> and (ConstantFn (lambda y (lambda x (call + (var x) (var y))))) []
                featurizeAndScoreDerivation(score=1) $Operator 1:2[and]: (derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))) [rule: $Operator -> and (ConstantFn (lambda y (lambda x (call + (var x) (var y)))))]
                addToChart $Operator: (derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyCatUnaryRules 1 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string and)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:1:2): 1 derivations {
                  $PHRASE(1,2): (string and) and, [score=0.0]
                }
                applyRule 1 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string and)) (type fb:type.text))]
                applyCatUnaryRules 1 2 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 1 2 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 1 2 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($LEMMA_PHRASE:1:2): 1 derivations {
                  $LEMMA_PHRASE(1,2): (string and) and, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:1:2): 1 derivations {
                  $TOKEN(1,2): (string and) and, [score=0.0]
                }
                ParserState.pruneCell($Operator:1:2): 2 derivations {
                  $Operator(1,2): (lambda y (lambda x (call + (var x) (var y)))) , [score=1.0]
                  $Operator(1,2): (lambda y (lambda x (call * (var x) (var y)))) , [score=-1.0]
                }
                ParserState.pruneCell($LEMMA_TOKEN:1:2): 1 derivations {
                  $LEMMA_TOKEN(1,2): (string and) and, [score=0.0]
                }
                applyNonCatUnaryRules(start=2, end=3, i=2, children=[], 0 rules)
                applyCatUnaryRules 2 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string four)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:2:3): 1 derivations {
                  $PHRASE(2,3): (string four) four, [score=0.0]
                }
                applyRule 2 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string four)) (type fb:type.text))]
                featurizeAndScoreDerivation(score=0) $Expr 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Expr -> $PHRASE (NumberFn)]
                addToChart $Expr: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Expr:2:3): 1 derivations {
                  $Expr(2,3): (number 4) , [score=0.0]
                }
                applyRule 2 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $Intermediate2 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate2:2:3): 1 derivations {
                  $Intermediate2(2,3): (number 4) , [score=0.0]
                }
                applyRule 2 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $Intermediate3 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate3:2:3): 1 derivations {
                  $Intermediate3(2,3): (number 4) , [score=0.0]
                }
                applyRule 2 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=0) $ROOT 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (number 4)) (type fb:type.int))
                ParserState.pruneCell($LEMMA_PHRASE:2:3): 1 derivations {
                  $LEMMA_PHRASE(2,3): (string four) four, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:2:3): 1 derivations {
                  $TOKEN(2,3): (string four) four, [score=0.0]
                }
                ParserState.pruneCell($ROOT:2:3): 1 derivations {
                  $ROOT(2,3): (number 4) , [score=0.0]
                }
                ParserState.pruneCell($LEMMA_TOKEN:2:3): 1 derivations {
                  $LEMMA_TOKEN(2,3): (string four) four, [score=0.0]
                }
                applyNonCatUnaryRules(start=0, end=2, i=0, children=[], 0 rules)
                applyNonCatUnaryRules(start=0, end=2, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=2, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyCatUnaryRules 0 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:2): 1 derivations {
                  $PHRASE(0,2): (string "three and") three and, [score=0.0]
                }
                applyRule 0 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and")) (type fb:type.text))]
                applyCatUnaryRules 0 2 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 0 2 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 0 2 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($LEMMA_PHRASE:0:2): 1 derivations {
                  $LEMMA_PHRASE(0,2): (string "three and") three and, [score=0.0]
                }
                applyNonCatUnaryRules(start=1, end=3, i=1, children=[], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[], 2 rules)
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=3, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))], 1 rules)
                applyRule 1 3 $Partial -> $Operator $Expr (JoinFn forward) [(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=1) $Partial 1:3[and four]: (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any))) [rule: $Partial -> $Operator $Expr (JoinFn forward)]
                addToChart $Partial: (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=3, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))], 1 rules)
                applyRule 1 3 $Partial -> $Operator $Expr (JoinFn forward) [(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=-1) $Partial 1:3[and four]: (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any))) [rule: $Partial -> $Operator $Expr (JoinFn forward)]
                addToChart $Partial: (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))
                applyCatUnaryRules 1 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "and four")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:1:3): 1 derivations {
                  $PHRASE(1,3): (string "and four") and four, [score=0.0]
                }
                applyRule 1 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "and four")) (type fb:type.text))]
                applyCatUnaryRules 1 3 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 1 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 1 3 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($Partial:1:3): 2 derivations {
                  $Partial(1,3): ((lambda y (lambda x (call + (var x) (var y)))) (number 4)) , [score=1.0]
                  $Partial(1,3): ((lambda y (lambda x (call * (var x) (var y)))) (number 4)) , [score=-1.0]
                }
                ParserState.pruneCell($LEMMA_PHRASE:1:3): 1 derivations {
                  $LEMMA_PHRASE(1,3): (string "and four") and four, [score=0.0]
                }
                applyNonCatUnaryRules(start=0, end=3, i=0, children=[], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))], 1 rules)
                applyRule 0 3 $Expr -> $Expr $Partial (JoinFn backward) [(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))]
                featurizeAndScoreDerivation(score=1) $Expr 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Expr -> $Expr $Partial (JoinFn backward)]
                addToChart $Expr: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))], 1 rules)
                applyRule 0 3 $Expr -> $Expr $Partial (JoinFn backward) [(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))]
                featurizeAndScoreDerivation(score=-1) $Expr 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Expr -> $Expr $Partial (JoinFn backward)]
                addToChart $Expr: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))], 0 rules)
                applyCatUnaryRules 0 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and four")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:3): 1 derivations {
                  $PHRASE(0,3): (string "three and four") three and four, [score=0.0]
                }
                applyRule 0 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and four")) (type fb:type.text))]
                applyCatUnaryRules 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Expr:0:3): 2 derivations {
                  $Expr(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=1.0]
                  $Expr(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=-1.0]
                }
                applyRule 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=1) $Intermediate2 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=-1) $Intermediate2 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyCatUnaryRules 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Intermediate2:0:3): 2 derivations {
                  $Intermediate2(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=1.0]
                  $Intermediate2(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=-1.0]
                }
                applyRule 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=1) $Intermediate3 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=-1) $Intermediate3 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyCatUnaryRules 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Intermediate3:0:3): 2 derivations {
                  $Intermediate3(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=1.0]
                  $Intermediate3(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=-1.0]
                }
                applyRule 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=1) $ROOT 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=-1) $ROOT 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                ParserState.pruneCell($LEMMA_PHRASE:0:3): 1 derivations {
                  $LEMMA_PHRASE(0,3): (string "three and four") three and four, [score=0.0]
                }
                ParserState.pruneCell($ROOT:0:3): 2 derivations {
                  $ROOT(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=1.0]
                  $ROOT(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=-1.0]
                }
              }
              Parser.ensureExecuted 
            }
            Parser.setEvaluation: 2 candidates {
              True@0000: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (value (number 7)) (type fb:type.any)) [score=1, prob=0.881, comp=1]
              Pred@0000: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (value (number 7)) (type fb:type.any)) [score=1, prob=0.881, comp=1]
              Pred@0001: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (value (number 12)) (type fb:type.any)) [score=-1, prob=0.119, comp=0]
            }
            Updating learner weights {
              L2 norm: 0.16857838899818123
            }
            Current: correct=1 oracle=1 partCorrect=1 partOracle=1 correctIndexAfterParse=0 correctMaxBeamPosition=0 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=45 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
            Cumulative(iter=1.train): correct=1 oracle=1 partCorrect=1 partOracle=1 correctIndexAfterParse=0 correctMaxBeamPosition=0 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=45 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
          }
        }
        Stats for iter=1.train: correct=1 oracle=1 partCorrect=1 partOracle=1 correctIndexAfterParse=0 correctMaxBeamPosition=0 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=45 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
        Evaluation stats for iter=1.train {
          correct = 1/ << 1 ~ 0 >> /1 (1)
          oracle = 1/ << 1 ~ 0 >> /1 (1)
          partCorrect = 1/ << 1 ~ 0 >> /1 (1)
          partOracle = 1/ << 1 ~ 0 >> /1 (1)
          correctIndexAfterParse = 0/ << 0 ~ 0 >> /0 (1)
          correctMaxBeamPosition = 0/ << 0 ~ 0 >> /0 (1)
          correctMaxUnsortedBeamPosition = 1/ << 1 ~ 0 >> /1 (1)
          parsed = 1/ << 1 ~ 0 >> /1 (1)
          numCandidates = 2/ << 2 ~ 0 >> /2 (1)
          parsedNumCandidates = 2/ << 2 ~ 0 >> /2 (1)
          numTokens = 3/ << 3 ~ 0 >> /3 (1)
          parseTime = 45/ << 45 ~ 0 >> /45 (1)
          maxCellSize = 2@$Operator:1:2/ << 2 ~ 0 >> /2@$Operator:1:2 (1)
          fallOffBeam = 0/ << 0 ~ 0 >> /0 (1)
          totalDerivs = 38/ << 38 ~ 0 >> /38 (1)
          numOfFeaturizedDerivs = 38/ << 38 ~ 0 >> /38 (1)
        }
      }
      StopWatchSet {
        FeatureExtractor.extractLocal	0.002s (0.0s x 76)
        NumberFn	0.011s (0.0s x 12)
        SelectFn	0.001s (0.0s x 16)
        IdentityFn	0.001s (0.0s x 8)
        ConstantFn	0.0s (0.0s x 4)
        JoinFn	0.002s (0.0s x 8)
        Executor.execute	0.003s (0.0s x 4)
        Parser.parse	0.14s (0.07s x 2)
        Learner.updateWeights	0.001s (0.0s x 2)
      }
      StopWatchSet {
        FeatureExtractor.extractLocal	0.002s (0.0s x 76)
        NumberFn	0.011s (0.0s x 12)
        SelectFn	0.001s (0.0s x 16)
        IdentityFn	0.001s (0.0s x 8)
        ConstantFn	0.0s (0.0s x 4)
        JoinFn	0.002s (0.0s x 8)
        Executor.execute	0.003s (0.0s x 4)
        Parser.parse	0.14s (0.07s x 2)
        Learner.updateWeights	0.001s (0.0s x 2)
      }
    }
    Iteration 2/3 {
      Processing iter=2.train: 1 examples {
        Examples {
          iter=2.train: example 0/1: data/tutorial-arithmetic.examples:0 {
            Example: three and four {
              Tokens: [three, and, four]
              Lemmatized tokens: [three, and, four]
              POS tags: [CD, UNK, CD]
              NER tags: [NUMBER, UNK, NUMBER]
              NER values: [3, UNK, 4]
              targetValue: (number 7)
              Dependency children: []
            }
            Parser.parse: parse {
              ParserState.infer {
                featurizeAndScoreDerivation(score=0) $TOKEN 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $TOKEN 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $TOKEN 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:2[three and]: (derivation (formula (string "three and")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "three and")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:2[three and]: (derivation (formula (string "three and")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "three and")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:3[three and four]: (derivation (formula (string "three and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "three and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:3[three and four]: (derivation (formula (string "three and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "three and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 1:3[and four]: (derivation (formula (string "and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 1:3[and four]: (derivation (formula (string "and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string four)) (type fb:type.text))
                applyNonCatUnaryRules(start=0, end=1, i=0, children=[], 0 rules)
                applyCatUnaryRules 0 1 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string three)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:1): 1 derivations {
                  $PHRASE(0,1): (string three) three, [score=0.0]
                }
                applyRule 0 1 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string three)) (type fb:type.text))]
                featurizeAndScoreDerivation(score=2) $Expr 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Expr -> $PHRASE (NumberFn)]
                addToChart $Expr: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Expr:0:1): 1 derivations {
                  $Expr(0,1): (number 3) , [score=2.0]
                }
                applyRule 0 1 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=4) $Intermediate2 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate2:0:1): 1 derivations {
                  $Intermediate2(0,1): (number 3) , [score=4.0]
                }
                applyRule 0 1 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=6) $Intermediate3 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate3:0:1): 1 derivations {
                  $Intermediate3(0,1): (number 3) , [score=6.0]
                }
                applyRule 0 1 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=8) $ROOT 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (number 3)) (type fb:type.int))
                ParserState.pruneCell($LEMMA_PHRASE:0:1): 1 derivations {
                  $LEMMA_PHRASE(0,1): (string three) three, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:0:1): 1 derivations {
                  $TOKEN(0,1): (string three) three, [score=0.0]
                }
                ParserState.pruneCell($ROOT:0:1): 1 derivations {
                  $ROOT(0,1): (number 3) , [score=8.0]
                }
                ParserState.pruneCell($LEMMA_TOKEN:0:1): 1 derivations {
                  $LEMMA_TOKEN(0,1): (string three) three, [score=0.0]
                }
                applyNonCatUnaryRules(start=1, end=2, i=1, children=[], 0 rules)
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[], 2 rules)
                applyRule 1 2 $Operator -> and (ConstantFn (lambda y (lambda x (call * (var x) (var y))))) []
                featurizeAndScoreDerivation(score=-0.232) $Operator 1:2[and]: (derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))) [rule: $Operator -> and (ConstantFn (lambda y (lambda x (call * (var x) (var y)))))]
                addToChart $Operator: (derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))
                applyRule 1 2 $Operator -> and (ConstantFn (lambda y (lambda x (call + (var x) (var y))))) []
                featurizeAndScoreDerivation(score=2.232) $Operator 1:2[and]: (derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))) [rule: $Operator -> and (ConstantFn (lambda y (lambda x (call + (var x) (var y)))))]
                addToChart $Operator: (derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyCatUnaryRules 1 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string and)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:1:2): 1 derivations {
                  $PHRASE(1,2): (string and) and, [score=0.0]
                }
                applyRule 1 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string and)) (type fb:type.text))]
                applyCatUnaryRules 1 2 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 1 2 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 1 2 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($LEMMA_PHRASE:1:2): 1 derivations {
                  $LEMMA_PHRASE(1,2): (string and) and, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:1:2): 1 derivations {
                  $TOKEN(1,2): (string and) and, [score=0.0]
                }
                ParserState.pruneCell($Operator:1:2): 2 derivations {
                  $Operator(1,2): (lambda y (lambda x (call + (var x) (var y)))) , [score=2.2319064464070966]
                  $Operator(1,2): (lambda y (lambda x (call * (var x) (var y)))) , [score=-0.23190644640709634]
                }
                ParserState.pruneCell($LEMMA_TOKEN:1:2): 1 derivations {
                  $LEMMA_TOKEN(1,2): (string and) and, [score=0.0]
                }
                applyNonCatUnaryRules(start=2, end=3, i=2, children=[], 0 rules)
                applyCatUnaryRules 2 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string four)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:2:3): 1 derivations {
                  $PHRASE(2,3): (string four) four, [score=0.0]
                }
                applyRule 2 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string four)) (type fb:type.text))]
                featurizeAndScoreDerivation(score=2) $Expr 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Expr -> $PHRASE (NumberFn)]
                addToChart $Expr: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Expr:2:3): 1 derivations {
                  $Expr(2,3): (number 4) , [score=2.0]
                }
                applyRule 2 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=4) $Intermediate2 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate2:2:3): 1 derivations {
                  $Intermediate2(2,3): (number 4) , [score=4.0]
                }
                applyRule 2 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=6) $Intermediate3 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate3:2:3): 1 derivations {
                  $Intermediate3(2,3): (number 4) , [score=6.0]
                }
                applyRule 2 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=8) $ROOT 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (number 4)) (type fb:type.int))
                ParserState.pruneCell($LEMMA_PHRASE:2:3): 1 derivations {
                  $LEMMA_PHRASE(2,3): (string four) four, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:2:3): 1 derivations {
                  $TOKEN(2,3): (string four) four, [score=0.0]
                }
                ParserState.pruneCell($ROOT:2:3): 1 derivations {
                  $ROOT(2,3): (number 4) , [score=8.0]
                }
                ParserState.pruneCell($LEMMA_TOKEN:2:3): 1 derivations {
                  $LEMMA_TOKEN(2,3): (string four) four, [score=0.0]
                }
                applyNonCatUnaryRules(start=0, end=2, i=0, children=[], 0 rules)
                applyNonCatUnaryRules(start=0, end=2, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=2, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyCatUnaryRules 0 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:2): 1 derivations {
                  $PHRASE(0,2): (string "three and") three and, [score=0.0]
                }
                applyRule 0 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and")) (type fb:type.text))]
                applyCatUnaryRules 0 2 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 0 2 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 0 2 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($LEMMA_PHRASE:0:2): 1 derivations {
                  $LEMMA_PHRASE(0,2): (string "three and") three and, [score=0.0]
                }
                applyNonCatUnaryRules(start=1, end=3, i=1, children=[], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[], 2 rules)
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=3, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))], 1 rules)
                applyRule 1 3 $Partial -> $Operator $Expr (JoinFn forward) [(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=6.232) $Partial 1:3[and four]: (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any))) [rule: $Partial -> $Operator $Expr (JoinFn forward)]
                addToChart $Partial: (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=3, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))], 1 rules)
                applyRule 1 3 $Partial -> $Operator $Expr (JoinFn forward) [(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=3.768) $Partial 1:3[and four]: (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any))) [rule: $Partial -> $Operator $Expr (JoinFn forward)]
                addToChart $Partial: (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))
                applyCatUnaryRules 1 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "and four")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:1:3): 1 derivations {
                  $PHRASE(1,3): (string "and four") and four, [score=0.0]
                }
                applyRule 1 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "and four")) (type fb:type.text))]
                applyCatUnaryRules 1 3 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 1 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 1 3 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($Partial:1:3): 2 derivations {
                  $Partial(1,3): ((lambda y (lambda x (call + (var x) (var y)))) (number 4)) , [score=6.231906446407097]
                  $Partial(1,3): ((lambda y (lambda x (call * (var x) (var y)))) (number 4)) , [score=3.7680935535929034]
                }
                ParserState.pruneCell($LEMMA_PHRASE:1:3): 1 derivations {
                  $LEMMA_PHRASE(1,3): (string "and four") and four, [score=0.0]
                }
                applyNonCatUnaryRules(start=0, end=3, i=0, children=[], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))], 1 rules)
                applyRule 0 3 $Expr -> $Expr $Partial (JoinFn backward) [(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))]
                featurizeAndScoreDerivation(score=10.232) $Expr 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Expr -> $Expr $Partial (JoinFn backward)]
                addToChart $Expr: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))], 1 rules)
                applyRule 0 3 $Expr -> $Expr $Partial (JoinFn backward) [(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))]
                featurizeAndScoreDerivation(score=7.768) $Expr 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Expr -> $Expr $Partial (JoinFn backward)]
                addToChart $Expr: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))], 0 rules)
                applyCatUnaryRules 0 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and four")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:3): 1 derivations {
                  $PHRASE(0,3): (string "three and four") three and four, [score=0.0]
                }
                applyRule 0 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and four")) (type fb:type.text))]
                applyCatUnaryRules 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Expr:0:3): 2 derivations {
                  $Expr(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=10.231906446407097]
                  $Expr(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=7.768093553592903]
                }
                applyRule 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=12.232) $Intermediate2 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=9.768) $Intermediate2 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyCatUnaryRules 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Intermediate2:0:3): 2 derivations {
                  $Intermediate2(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=12.231906446407097]
                  $Intermediate2(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=9.768093553592903]
                }
                applyRule 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=14.232) $Intermediate3 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=11.768) $Intermediate3 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyCatUnaryRules 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Intermediate3:0:3): 2 derivations {
                  $Intermediate3(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=14.231906446407097]
                  $Intermediate3(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=11.768093553592903]
                }
                applyRule 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=16.232) $ROOT 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=13.768) $ROOT 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                ParserState.pruneCell($LEMMA_PHRASE:0:3): 1 derivations {
                  $LEMMA_PHRASE(0,3): (string "three and four") three and four, [score=0.0]
                }
                ParserState.pruneCell($ROOT:0:3): 2 derivations {
                  $ROOT(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=16.231906446407095]
                  $ROOT(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=13.768093553592903]
                }
              }
              Parser.ensureExecuted 
            }
            Parser.setEvaluation: 2 candidates {
              True@0000: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (value (number 7)) (type fb:type.any)) [score=16.232, prob=0.922, comp=1]
              Pred@0000: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (value (number 7)) (type fb:type.any)) [score=16.232, prob=0.922, comp=1]
              Pred@0001: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (value (number 12)) (type fb:type.any)) [score=13.768, prob=0.078, comp=0]
            }
            Updating learner weights {
              L2 norm: 0.11092283516205845
            }
            Current: correct=1 oracle=1 partCorrect=1 partOracle=1 correctIndexAfterParse=0 correctMaxBeamPosition=0 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=37 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
            Cumulative(iter=2.train): correct=1 oracle=1 partCorrect=1 partOracle=1 correctIndexAfterParse=0 correctMaxBeamPosition=0 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=37 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
          }
        }
        Stats for iter=2.train: correct=1 oracle=1 partCorrect=1 partOracle=1 correctIndexAfterParse=0 correctMaxBeamPosition=0 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=37 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
        Evaluation stats for iter=2.train {
          correct = 1/ << 1 ~ 0 >> /1 (1)
          oracle = 1/ << 1 ~ 0 >> /1 (1)
          partCorrect = 1/ << 1 ~ 0 >> /1 (1)
          partOracle = 1/ << 1 ~ 0 >> /1 (1)
          correctIndexAfterParse = 0/ << 0 ~ 0 >> /0 (1)
          correctMaxBeamPosition = 0/ << 0 ~ 0 >> /0 (1)
          correctMaxUnsortedBeamPosition = 1/ << 1 ~ 0 >> /1 (1)
          parsed = 1/ << 1 ~ 0 >> /1 (1)
          numCandidates = 2/ << 2 ~ 0 >> /2 (1)
          parsedNumCandidates = 2/ << 2 ~ 0 >> /2 (1)
          numTokens = 3/ << 3 ~ 0 >> /3 (1)
          parseTime = 37/ << 37 ~ 0 >> /37 (1)
          maxCellSize = 2@$Operator:1:2/ << 2 ~ 0 >> /2@$Operator:1:2 (1)
          fallOffBeam = 0/ << 0 ~ 0 >> /0 (1)
          totalDerivs = 38/ << 38 ~ 0 >> /38 (1)
          numOfFeaturizedDerivs = 38/ << 38 ~ 0 >> /38 (1)
        }
      }
      StopWatchSet {
        FeatureExtractor.extractLocal	0.002s (0.0s x 114)
        NumberFn	0.011s (0.0s x 18)
        SelectFn	0.001s (0.0s x 24)
        IdentityFn	0.001s (0.0s x 12)
        ConstantFn	0.0s (0.0s x 6)
        JoinFn	0.002s (0.0s x 12)
        Executor.execute	0.003s (0.0s x 6)
        Parser.parse	0.178s (0.059s x 3)
        Learner.updateWeights	0.001s (0.0s x 3)
      }
      StopWatchSet {
        FeatureExtractor.extractLocal	0.002s (0.0s x 114)
        NumberFn	0.011s (0.0s x 18)
        SelectFn	0.001s (0.0s x 24)
        IdentityFn	0.001s (0.0s x 12)
        ConstantFn	0.0s (0.0s x 6)
        JoinFn	0.002s (0.0s x 12)
        Executor.execute	0.003s (0.0s x 6)
        Parser.parse	0.178s (0.059s x 3)
        Learner.updateWeights	0.001s (0.0s x 3)
      }
    }
    Iteration 3/3 {
      Processing iter=3.train: 1 examples {
        Examples {
          iter=3.train: example 0/1: data/tutorial-arithmetic.examples:0 {
            Example: three and four {
              Tokens: [three, and, four]
              Lemmatized tokens: [three, and, four]
              POS tags: [CD, UNK, CD]
              NER tags: [NUMBER, UNK, NUMBER]
              NER values: [3, UNK, 4]
              targetValue: (number 7)
              Dependency children: []
            }
            Parser.parse: parse {
              ParserState.infer {
                featurizeAndScoreDerivation(score=0) $TOKEN 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $TOKEN 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $TOKEN 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $TOKEN: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_TOKEN 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_TOKEN: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:1[three]: (derivation (formula (string three)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string three)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:2[three and]: (derivation (formula (string "three and")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "three and")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:2[three and]: (derivation (formula (string "three and")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "three and")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 0:3[three and four]: (derivation (formula (string "three and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "three and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 0:3[three and four]: (derivation (formula (string "three and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "three and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 1:2[and]: (derivation (formula (string and)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string and)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 1:3[and four]: (derivation (formula (string "and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string "and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 1:3[and four]: (derivation (formula (string "and four")) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string "and four")) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $PHRASE 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $PHRASE: (derivation (formula (string four)) (type fb:type.text))
                featurizeAndScoreDerivation(score=0) $LEMMA_PHRASE 2:3[four]: (derivation (formula (string four)) (type fb:type.text)) [rule: null ->  null]
                addToChart $LEMMA_PHRASE: (derivation (formula (string four)) (type fb:type.text))
                applyNonCatUnaryRules(start=0, end=1, i=0, children=[], 0 rules)
                applyCatUnaryRules 0 1 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string three)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:1): 1 derivations {
                  $PHRASE(0,1): (string three) three, [score=0.0]
                }
                applyRule 0 1 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string three)) (type fb:type.text))]
                featurizeAndScoreDerivation(score=2.310) $Expr 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Expr -> $PHRASE (NumberFn)]
                addToChart $Expr: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Expr:0:1): 1 derivations {
                  $Expr(0,1): (number 3) , [score=2.309662726298916]
                }
                applyRule 0 1 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=4.619) $Intermediate2 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate2:0:1): 1 derivations {
                  $Intermediate2(0,1): (number 3) , [score=4.619325452597832]
                }
                applyRule 0 1 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=6.929) $Intermediate3 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (number 3)) (type fb:type.int))
                applyCatUnaryRules 0 1 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 3)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate3:0:1): 1 derivations {
                  $Intermediate3(0,1): (number 3) , [score=6.9289881788967485]
                }
                applyRule 0 1 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 3)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=9.239) $ROOT 0:1[three]: (derivation (formula (number 3)) (type fb:type.int)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (number 3)) (type fb:type.int))
                ParserState.pruneCell($LEMMA_PHRASE:0:1): 1 derivations {
                  $LEMMA_PHRASE(0,1): (string three) three, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:0:1): 1 derivations {
                  $TOKEN(0,1): (string three) three, [score=0.0]
                }
                ParserState.pruneCell($ROOT:0:1): 1 derivations {
                  $ROOT(0,1): (number 3) , [score=9.238650905195664]
                }
                ParserState.pruneCell($LEMMA_TOKEN:0:1): 1 derivations {
                  $LEMMA_TOKEN(0,1): (string three) three, [score=0.0]
                }
                applyNonCatUnaryRules(start=1, end=2, i=1, children=[], 0 rules)
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[], 2 rules)
                applyRule 1 2 $Operator -> and (ConstantFn (lambda y (lambda x (call * (var x) (var y))))) []
                featurizeAndScoreDerivation(score=-0.269) $Operator 1:2[and]: (derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))) [rule: $Operator -> and (ConstantFn (lambda y (lambda x (call * (var x) (var y)))))]
                addToChart $Operator: (derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))
                applyRule 1 2 $Operator -> and (ConstantFn (lambda y (lambda x (call + (var x) (var y))))) []
                featurizeAndScoreDerivation(score=2.496) $Operator 1:2[and]: (derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))) [rule: $Operator -> and (ConstantFn (lambda y (lambda x (call + (var x) (var y)))))]
                addToChart $Operator: (derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=2, i=2, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyCatUnaryRules 1 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string and)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:1:2): 1 derivations {
                  $PHRASE(1,2): (string and) and, [score=0.0]
                }
                applyRule 1 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string and)) (type fb:type.text))]
                applyCatUnaryRules 1 2 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 1 2 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 1 2 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($LEMMA_PHRASE:1:2): 1 derivations {
                  $LEMMA_PHRASE(1,2): (string and) and, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:1:2): 1 derivations {
                  $TOKEN(1,2): (string and) and, [score=0.0]
                }
                ParserState.pruneCell($Operator:1:2): 2 derivations {
                  $Operator(1,2): (lambda y (lambda x (call + (var x) (var y)))) , [score=2.4962990107816676]
                  $Operator(1,2): (lambda y (lambda x (call * (var x) (var y)))) , [score=-0.26920582846020347]
                }
                ParserState.pruneCell($LEMMA_TOKEN:1:2): 1 derivations {
                  $LEMMA_TOKEN(1,2): (string and) and, [score=0.0]
                }
                applyNonCatUnaryRules(start=2, end=3, i=2, children=[], 0 rules)
                applyCatUnaryRules 2 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string four)) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:2:3): 1 derivations {
                  $PHRASE(2,3): (string four) four, [score=0.0]
                }
                applyRule 2 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string four)) (type fb:type.text))]
                featurizeAndScoreDerivation(score=2.310) $Expr 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Expr -> $PHRASE (NumberFn)]
                addToChart $Expr: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Expr:2:3): 1 derivations {
                  $Expr(2,3): (number 4) , [score=2.309662726298916]
                }
                applyRule 2 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=4.619) $Intermediate2 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate2:2:3): 1 derivations {
                  $Intermediate2(2,3): (number 4) , [score=4.619325452597832]
                }
                applyRule 2 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=6.929) $Intermediate3 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (number 4)) (type fb:type.int))
                applyCatUnaryRules 2 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 4)) (type fb:type.int))]
                ParserState.pruneCell($Intermediate3:2:3): 1 derivations {
                  $Intermediate3(2,3): (number 4) , [score=6.9289881788967485]
                }
                applyRule 2 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=9.239) $ROOT 2:3[four]: (derivation (formula (number 4)) (type fb:type.int)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (number 4)) (type fb:type.int))
                ParserState.pruneCell($LEMMA_PHRASE:2:3): 1 derivations {
                  $LEMMA_PHRASE(2,3): (string four) four, [score=0.0]
                }
                ParserState.pruneCell($TOKEN:2:3): 1 derivations {
                  $TOKEN(2,3): (string four) four, [score=0.0]
                }
                ParserState.pruneCell($ROOT:2:3): 1 derivations {
                  $ROOT(2,3): (number 4) , [score=9.238650905195664]
                }
                ParserState.pruneCell($LEMMA_TOKEN:2:3): 1 derivations {
                  $LEMMA_TOKEN(2,3): (string four) four, [score=0.0]
                }
                applyNonCatUnaryRules(start=0, end=2, i=0, children=[], 0 rules)
                applyNonCatUnaryRules(start=0, end=2, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=2, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyCatUnaryRules 0 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:2): 1 derivations {
                  $PHRASE(0,2): (string "three and") three and, [score=0.0]
                }
                applyRule 0 2 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and")) (type fb:type.text))]
                applyCatUnaryRules 0 2 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 0 2 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 0 2 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($LEMMA_PHRASE:0:2): 1 derivations {
                  $LEMMA_PHRASE(0,2): (string "three and") three and, [score=0.0]
                }
                applyNonCatUnaryRules(start=1, end=3, i=1, children=[], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[], 2 rules)
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=3, children=[(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))], 1 rules)
                applyRule 1 3 $Partial -> $Operator $Expr (JoinFn forward) [(derivation (formula (lambda y (lambda x (call + (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=7.116) $Partial 1:3[and four]: (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any))) [rule: $Partial -> $Operator $Expr (JoinFn forward)]
                addToChart $Partial: (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))
                applyNonCatUnaryRules(start=1, end=3, i=2, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any))))], 0 rules)
                applyNonCatUnaryRules(start=1, end=3, i=3, children=[(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))], 1 rules)
                applyRule 1 3 $Partial -> $Operator $Expr (JoinFn forward) [(derivation (formula (lambda y (lambda x (call * (var x) (var y))))) (type (-> top (-> top fb:type.any)))), (derivation (formula (number 4)) (type fb:type.int))]
                featurizeAndScoreDerivation(score=4.350) $Partial 1:3[and four]: (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any))) [rule: $Partial -> $Operator $Expr (JoinFn forward)]
                addToChart $Partial: (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))
                applyCatUnaryRules 1 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "and four")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:1:3): 1 derivations {
                  $PHRASE(1,3): (string "and four") and four, [score=0.0]
                }
                applyRule 1 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "and four")) (type fb:type.text))]
                applyCatUnaryRules 1 3 $Intermediate2 -> $Expr (SelectFn 0) null
                applyCatUnaryRules 1 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) null
                applyCatUnaryRules 1 3 $ROOT -> $Intermediate3 (IdentityFn) null
                ParserState.pruneCell($Partial:1:3): 2 derivations {
                  $Partial(1,3): ((lambda y (lambda x (call + (var x) (var y)))) (number 4)) , [score=7.115624463379499]
                  $Partial(1,3): ((lambda y (lambda x (call * (var x) (var y)))) (number 4)) , [score=4.350119624137628]
                }
                ParserState.pruneCell($LEMMA_PHRASE:1:3): 1 derivations {
                  $LEMMA_PHRASE(1,3): (string "and four") and four, [score=0.0]
                }
                applyNonCatUnaryRules(start=0, end=3, i=0, children=[], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=1, children=[(derivation (formula (number 3)) (type fb:type.int))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))], 1 rules)
                applyRule 0 3 $Expr -> $Expr $Partial (JoinFn backward) [(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call + (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))]
                featurizeAndScoreDerivation(score=11.735) $Expr 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Expr -> $Expr $Partial (JoinFn backward)]
                addToChart $Expr: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))], 1 rules)
                applyRule 0 3 $Expr -> $Expr $Partial (JoinFn backward) [(derivation (formula (number 3)) (type fb:type.int)), (derivation (formula ((lambda y (lambda x (call * (var x) (var y)))) (number 4))) (type (-> top fb:type.any)))]
                featurizeAndScoreDerivation(score=8.969) $Expr 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Expr -> $Expr $Partial (JoinFn backward)]
                addToChart $Expr: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))], 0 rules)
                applyNonCatUnaryRules(start=0, end=3, i=3, children=[(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))], 0 rules)
                applyCatUnaryRules 0 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and four")) (type fb:type.text))]
                ParserState.pruneCell($PHRASE:0:3): 1 derivations {
                  $PHRASE(0,3): (string "three and four") three and four, [score=0.0]
                }
                applyRule 0 3 $Expr -> $PHRASE (NumberFn) [(derivation (formula (string "three and four")) (type fb:type.text))]
                applyCatUnaryRules 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Expr:0:3): 2 derivations {
                  $Expr(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=11.734949915977332]
                  $Expr(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=8.969445076735461]
                }
                applyRule 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=14.045) $Intermediate2 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $Intermediate2 -> $Expr (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=11.279) $Intermediate2 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate2 -> $Expr (SelectFn 0)]
                addToChart $Intermediate2: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyCatUnaryRules 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Intermediate2:0:3): 2 derivations {
                  $Intermediate2(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=14.044612642276247]
                  $Intermediate2(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=11.279107803034377]
                }
                applyRule 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=16.354) $Intermediate3 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $Intermediate3 -> $Intermediate2 (SelectFn 0) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=13.589) $Intermediate3 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $Intermediate3 -> $Intermediate2 (SelectFn 0)]
                addToChart $Intermediate3: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyCatUnaryRules 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)), (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                ParserState.pruneCell($Intermediate3:0:3): 2 derivations {
                  $Intermediate3(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=16.354275368575163]
                  $Intermediate3(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=13.588770529333292]
                }
                applyRule 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=18.664) $ROOT 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                applyRule 0 3 $ROOT -> $Intermediate3 (IdentityFn) [(derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))]
                featurizeAndScoreDerivation(score=15.898) $ROOT 0:3[three and four]: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any)) [rule: $ROOT -> $Intermediate3 (IdentityFn)]
                addToChart $ROOT: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (type fb:type.any))
                ParserState.pruneCell($LEMMA_PHRASE:0:3): 1 derivations {
                  $LEMMA_PHRASE(0,3): (string "three and four") three and four, [score=0.0]
                }
                ParserState.pruneCell($ROOT:0:3): 2 derivations {
                  $ROOT(0,3): (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3)) , [score=18.66393809487408]
                  $ROOT(0,3): (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3)) , [score=15.898433255632208]
                }
              }
              Parser.ensureExecuted 
            }
            Parser.setEvaluation: 2 candidates {
              True@0000: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (value (number 7)) (type fb:type.any)) [score=18.664, prob=0.941, comp=1]
              Pred@0000: (derivation (formula (((lambda y (lambda x (call + (var x) (var y)))) (number 4)) (number 3))) (value (number 7)) (type fb:type.any)) [score=18.664, prob=0.941, comp=1]
              Pred@0001: (derivation (formula (((lambda y (lambda x (call * (var x) (var y)))) (number 4)) (number 3))) (value (number 12)) (type fb:type.any)) [score=15.898, prob=0.059, comp=0]
            }
            Current: correct=1 oracle=1 partCorrect=1 partOracle=1 correctIndexAfterParse=0 correctMaxBeamPosition=0 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=39 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
            Cumulative(iter=3.train): correct=1 oracle=1 partCorrect=1 partOracle=1 correctIndexAfterParse=0 correctMaxBeamPosition=0 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=39 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
          }
        }
        Stats for iter=3.train: correct=1 oracle=1 partCorrect=1 partOracle=1 correctIndexAfterParse=0 correctMaxBeamPosition=0 correctMaxUnsortedBeamPosition=1 parsed=1 numCandidates=2 parsedNumCandidates=2 numTokens=3 parseTime=39 maxCellSize=2 fallOffBeam=0 totalDerivs=38 numOfFeaturizedDerivs=38
        Evaluation stats for iter=3.train {
          correct = 1/ << 1 ~ 0 >> /1 (1)
          oracle = 1/ << 1 ~ 0 >> /1 (1)
          partCorrect = 1/ << 1 ~ 0 >> /1 (1)
          partOracle = 1/ << 1 ~ 0 >> /1 (1)
          correctIndexAfterParse = 0/ << 0 ~ 0 >> /0 (1)
          correctMaxBeamPosition = 0/ << 0 ~ 0 >> /0 (1)
          correctMaxUnsortedBeamPosition = 1/ << 1 ~ 0 >> /1 (1)
          parsed = 1/ << 1 ~ 0 >> /1 (1)
          numCandidates = 2/ << 2 ~ 0 >> /2 (1)
          parsedNumCandidates = 2/ << 2 ~ 0 >> /2 (1)
          numTokens = 3/ << 3 ~ 0 >> /3 (1)
          parseTime = 39/ << 39 ~ 0 >> /39 (1)
          maxCellSize = 2@$Operator:1:2/ << 2 ~ 0 >> /2@$Operator:1:2 (1)
          fallOffBeam = 0/ << 0 ~ 0 >> /0 (1)
          totalDerivs = 38/ << 38 ~ 0 >> /38 (1)
          numOfFeaturizedDerivs = 38/ << 38 ~ 0 >> /38 (1)
        }
      }
      StopWatchSet {
        FeatureExtractor.extractLocal	0.003s (0.0s x 152)
        NumberFn	0.011s (0.0s x 24)
        SelectFn	0.001s (0.0s x 32)
        IdentityFn	0.001s (0.0s x 16)
        ConstantFn	0.0s (0.0s x 8)
        JoinFn	0.002s (0.0s x 16)
        Executor.execute	0.003s (0.0s x 8)
        Parser.parse	0.218s (0.054s x 4)
        Learner.updateWeights	0.001s (0.0s x 3)
      }
      StopWatchSet {
        FeatureExtractor.extractLocal	0.003s (0.0s x 152)
        NumberFn	0.011s (0.0s x 24)
        SelectFn	0.001s (0.0s x 32)
        IdentityFn	0.001s (0.0s x 16)
        ConstantFn	0.0s (0.0s x 8)
        JoinFn	0.002s (0.0s x 16)
        Executor.execute	0.003s (0.0s x 8)
        Parser.parse	0.218s (0.054s x 4)
        Learner.updateWeights	0.001s (0.0s x 3)
      }
    }
  }
  Enter an utterance to parse or one of the following commands:
    (help): show this help message
    (status): prints out status of the system
    (get |option|): get a command-line option (e.g., (get Parser.verbose))
    (set |option| |value|): set a command-line option (e.g., (set Parser.verbose 5))
    (reload): reload the grammar/parameters
    (grammar): prints out the grammar
    (params [|file|]): dumps all the model parameters
    (select |candidate index|): show information about the |index|-th candidate of the last utterance.
    (accept |candidate index|): record the |index|-th candidate as the correct answer for the last utterance.
    (answer |answer|): record |answer| as the correct answer for the last utterance (e.g., (answer (list (number 3)))).
    (rule |lhs| (|rhs_1| ... |rhs_k|) |sem|): adds a rule to the grammar (e.g., (rule $Number ($TOKEN) (NumberFn)))
    (type |logical form|): perform type inference (e.g., (type (number 3)))
    (execute |logical form|): execute the logical form (e.g., (execute (call + (number 3) (number 4))))
    (def |key| |value|): define a macro to replace |key| with |value| in all commands (e.g., (def type fb:type.object type)))
    (context [(user |user|) (date |date|) (exchange |exchange|) (graph |graph|)]): prints out or set the context
  Press Ctrl-D to exit.
> ProcessManager: interrupted
Command failed: java -cp libsempre/*:lib/* -ea edu.stanford.nlp.sempre.Main -Main.interactive -Parser.verbose 5 -Parser.visualizeChartFilling true -Grammar.inPaths data/tutorial-arithmetic.grammar -FeatureExtractor.featureDomains rule -Dataset.inPaths train:data/tutorial-arithmetic.examples -Learner.maxTrainIters 3
ProcessManager: killing child processes to avoid orphaning: 24162
```
