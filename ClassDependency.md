The result of the running command `jdeps -v -package edu.stanford.nlp.sempre *.class` at the directory contains class files. We strongly recommend you to use `grep` to find something.

**Note that the dependency does not include annotation like** `@Option public String executor = "JavaExecutor";`

```jdeps
AbstractReinforcementParserState.class -> ChartParserState$CatSpan.class
AbstractReinforcementParserState.class -> ChartParserState.class
AbstractReinforcementParserState.class -> CoarseParser$CoarseParserState.class
AbstractReinforcementParserState.class -> CoarseParser.class
AbstractReinforcementParserState.class -> Derivation.class
AbstractReinforcementParserState.class -> DerivationStream.class
AbstractReinforcementParserState.class -> Example.class
AbstractReinforcementParserState.class -> Params.class
AbstractReinforcementParserState.class -> Parser$Options.class
AbstractReinforcementParserState.class -> Parser.class
AbstractReinforcementParserState.class -> ReinforcementParser.class
AbstractReinforcementParserState.class -> Rule.class
AbstractReinforcementParserState.class -> SemanticFn$CallInfo.class
AbstractReinforcementParserState.class -> SemanticFn$Callable.class
AbstractReinforcementParserState.class -> SemanticFn.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.ChartParserState           ChartParserState.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.ChartParserState$CatSpan   ChartParserState$CatSpan.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.CoarseParser               CoarseParser.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.CoarseParser$CoarseParserState CoarseParser$CoarseParserState.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.Parser$Options             Parser$Options.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.ReinforcementParser        ReinforcementParser.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.SemanticFn$CallInfo        SemanticFn$CallInfo.class
   edu.stanford.nlp.sempre.AbstractReinforcementParserState -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
AggregateFormula$Mode.class -> AggregateFormula.class
   edu.stanford.nlp.sempre.AggregateFormula$Mode      -> edu.stanford.nlp.sempre.AggregateFormula           AggregateFormula.class
AggregateFormula.class -> AggregateFormula$Mode.class
AggregateFormula.class -> Formula.class
   edu.stanford.nlp.sempre.AggregateFormula           -> edu.stanford.nlp.sempre.AggregateFormula$Mode      AggregateFormula$Mode.class
   edu.stanford.nlp.sempre.AggregateFormula           -> edu.stanford.nlp.sempre.Formula                    Formula.class
AllFeatureMatcher.class -> FeatureMatcher.class
   edu.stanford.nlp.sempre.AllFeatureMatcher          -> edu.stanford.nlp.sempre.FeatureMatcher             FeatureMatcher.class
ArithmeticFormula$1.class -> ArithmeticFormula$Mode.class
ArithmeticFormula$1.class -> ArithmeticFormula.class
   edu.stanford.nlp.sempre.ArithmeticFormula$1        -> edu.stanford.nlp.sempre.ArithmeticFormula          ArithmeticFormula.class
   edu.stanford.nlp.sempre.ArithmeticFormula$1        -> edu.stanford.nlp.sempre.ArithmeticFormula$Mode     ArithmeticFormula$Mode.class
ArithmeticFormula$Mode.class -> ArithmeticFormula.class
   edu.stanford.nlp.sempre.ArithmeticFormula$Mode     -> edu.stanford.nlp.sempre.ArithmeticFormula          ArithmeticFormula.class
ArithmeticFormula.class -> ArithmeticFormula$1.class
ArithmeticFormula.class -> ArithmeticFormula$Mode.class
ArithmeticFormula.class -> Formula.class
   edu.stanford.nlp.sempre.ArithmeticFormula          -> edu.stanford.nlp.sempre.ArithmeticFormula$1        ArithmeticFormula$1.class
   edu.stanford.nlp.sempre.ArithmeticFormula          -> edu.stanford.nlp.sempre.ArithmeticFormula$Mode     ArithmeticFormula$Mode.class
   edu.stanford.nlp.sempre.ArithmeticFormula          -> edu.stanford.nlp.sempre.Formula                    Formula.class
AtomicSemType.class -> SemType.class
AtomicSemType.class -> SemTypeHierarchy.class
AtomicSemType.class -> TopSemType.class
AtomicSemType.class -> UnionSemType.class
   edu.stanford.nlp.sempre.AtomicSemType              -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.AtomicSemType              -> edu.stanford.nlp.sempre.SemTypeHierarchy           SemTypeHierarchy.class
   edu.stanford.nlp.sempre.AtomicSemType              -> edu.stanford.nlp.sempre.TopSemType                 TopSemType.class
   edu.stanford.nlp.sempre.AtomicSemType              -> edu.stanford.nlp.sempre.UnionSemType               UnionSemType.class
BeamParser$Options.class -> BeamParser.class
   edu.stanford.nlp.sempre.BeamParser$Options         -> edu.stanford.nlp.sempre.BeamParser                 BeamParser.class
BeamParser.class -> BeamParser$Options.class
BeamParser.class -> BeamParserState$Mode.class
BeamParser.class -> BeamParserState.class
BeamParser.class -> Example.class
BeamParser.class -> Grammar.class
BeamParser.class -> Params.class
BeamParser.class -> Parser$Options.class
BeamParser.class -> Parser$Spec.class
BeamParser.class -> Parser.class
BeamParser.class -> ParserState.class
BeamParser.class -> Rule.class
BeamParser.class -> Trie.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.BeamParser$Options         BeamParser$Options.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.BeamParserState            BeamParserState.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.BeamParserState$Mode       BeamParserState$Mode.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.Grammar                    Grammar.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.Parser$Options             Parser$Options.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.Parser$Spec                Parser$Spec.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.BeamParser                 -> edu.stanford.nlp.sempre.Trie                       Trie.class
BeamParserState$Mode.class -> BeamParserState.class
   edu.stanford.nlp.sempre.BeamParserState$Mode       -> edu.stanford.nlp.sempre.BeamParserState            BeamParserState.class
BeamParserState.class -> BeamParser$Options.class
BeamParserState.class -> BeamParser.class
BeamParserState.class -> BeamParserState$Mode.class
BeamParserState.class -> ChartParserState$ChartFillingData.class
BeamParserState.class -> ChartParserState.class
BeamParserState.class -> Derivation$Builder.class
BeamParserState.class -> Derivation.class
BeamParserState.class -> DerivationStream.class
BeamParserState.class -> Example.class
BeamParserState.class -> Formula.class
BeamParserState.class -> Json.class
BeamParserState.class -> Params.class
BeamParserState.class -> Parser$Options.class
BeamParserState.class -> Parser.class
BeamParserState.class -> ParserState.class
BeamParserState.class -> Rule.class
BeamParserState.class -> SemanticFn$CallInfo.class
BeamParserState.class -> SemanticFn$Callable.class
BeamParserState.class -> SemanticFn.class
BeamParserState.class -> Trie.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.BeamParser                 BeamParser.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.BeamParser$Options         BeamParser$Options.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.BeamParserState$Mode       BeamParserState$Mode.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.ChartParserState           ChartParserState.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.ChartParserState$ChartFillingData ChartParserState$ChartFillingData.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.Json                       Json.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.Parser$Options             Parser$Options.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.SemanticFn$CallInfo        SemanticFn$CallInfo.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.BeamParserState            -> edu.stanford.nlp.sempre.Trie                       Trie.class
BooleanValue.class -> Value.class
   edu.stanford.nlp.sempre.BooleanValue               -> edu.stanford.nlp.sempre.Value                      Value.class
BoundedPriorityQueue$1.class -> BoundedPriorityQueue.class
   edu.stanford.nlp.sempre.BoundedPriorityQueue$1     -> edu.stanford.nlp.sempre.BoundedPriorityQueue       BoundedPriorityQueue.class
BoundedPriorityQueue.class -> BoundedPriorityQueue$1.class
   edu.stanford.nlp.sempre.BoundedPriorityQueue       -> edu.stanford.nlp.sempre.BoundedPriorityQueue$1     BoundedPriorityQueue$1.class
Builder$Options.class -> Builder.class
   edu.stanford.nlp.sempre.Builder$Options            -> edu.stanford.nlp.sempre.Builder                    Builder.class
Builder.class -> BeamParser.class
Builder.class -> Builder$Options.class
Builder.class -> Executor.class
Builder.class -> FeatureExtractor.class
Builder.class -> FloatingParser.class
Builder.class -> Grammar.class
Builder.class -> Params.class
Builder.class -> Parser$Spec.class
Builder.class -> Parser.class
Builder.class -> ReinforcementParser.class
Builder.class -> SempreUtils.class
Builder.class -> ValueEvaluator.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.BeamParser                 BeamParser.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.Builder$Options            Builder$Options.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.FloatingParser             FloatingParser.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.Grammar                    Grammar.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.Parser$Spec                Parser$Spec.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.ReinforcementParser        ReinforcementParser.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.SempreUtils                SempreUtils.class
   edu.stanford.nlp.sempre.Builder                    -> edu.stanford.nlp.sempre.ValueEvaluator             ValueEvaluator.class
CallFormula.class -> Formula.class
CallFormula.class -> Formulas.class
CallFormula.class -> ValueFormula.class
   edu.stanford.nlp.sempre.CallFormula                -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.CallFormula                -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.CallFormula                -> edu.stanford.nlp.sempre.ValueFormula               ValueFormula.class
CallTypeInfo.class -> SemType.class
   edu.stanford.nlp.sempre.CallTypeInfo               -> edu.stanford.nlp.sempre.SemType                    SemType.class
ChartParserState$CatSpan.class -> ChartParserState.class
   edu.stanford.nlp.sempre.ChartParserState$CatSpan   -> edu.stanford.nlp.sempre.ChartParserState           ChartParserState.class
ChartParserState$ChartFillingData.class -> ChartParserState$CatSpan.class
ChartParserState$ChartFillingData.class -> ChartParserState.class
   edu.stanford.nlp.sempre.ChartParserState$ChartFillingData -> edu.stanford.nlp.sempre.ChartParserState           ChartParserState.class
   edu.stanford.nlp.sempre.ChartParserState$ChartFillingData -> edu.stanford.nlp.sempre.ChartParserState$CatSpan   ChartParserState$CatSpan.class
ChartParserState.class -> ChartParserState$CatSpan.class
ChartParserState.class -> ChartParserState$ChartFillingData.class
ChartParserState.class -> Derivation.class
ChartParserState.class -> ErrorValue.class
ChartParserState.class -> Example.class
ChartParserState.class -> LanguageInfo.class
ChartParserState.class -> Params.class
ChartParserState.class -> Parser$Options.class
ChartParserState.class -> Parser.class
ChartParserState.class -> ParserState.class
ChartParserState.class -> Rule.class
ChartParserState.class -> Value.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.ChartParserState$CatSpan   ChartParserState$CatSpan.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.ChartParserState$ChartFillingData ChartParserState$ChartFillingData.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.ErrorValue                 ErrorValue.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.Parser$Options             Parser$Options.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.ChartParserState           -> edu.stanford.nlp.sempre.Value                      Value.class
CoarseParser$CategorySpan.class -> CoarseParser.class
   edu.stanford.nlp.sempre.CoarseParser$CategorySpan  -> edu.stanford.nlp.sempre.CoarseParser               CoarseParser.class
CoarseParser$CoarseParserState.class -> CoarseParser$CategorySpan.class
CoarseParser$CoarseParserState.class -> CoarseParser.class
CoarseParser$CoarseParserState.class -> Example.class
CoarseParser$CoarseParserState.class -> LanguageInfo.class
CoarseParser$CoarseParserState.class -> Parser$Options.class
CoarseParser$CoarseParserState.class -> Parser.class
CoarseParser$CoarseParserState.class -> Rule.class
   edu.stanford.nlp.sempre.CoarseParser$CoarseParserState -> edu.stanford.nlp.sempre.CoarseParser               CoarseParser.class
   edu.stanford.nlp.sempre.CoarseParser$CoarseParserState -> edu.stanford.nlp.sempre.CoarseParser$CategorySpan  CoarseParser$CategorySpan.class
   edu.stanford.nlp.sempre.CoarseParser$CoarseParserState -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.CoarseParser$CoarseParserState -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.CoarseParser$CoarseParserState -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.CoarseParser$CoarseParserState -> edu.stanford.nlp.sempre.Parser$Options             Parser$Options.class
   edu.stanford.nlp.sempre.CoarseParser$CoarseParserState -> edu.stanford.nlp.sempre.Rule                       Rule.class
CoarseParser.class -> CoarseParser$CategorySpan.class
CoarseParser.class -> CoarseParser$CoarseParserState.class
CoarseParser.class -> Example.class
CoarseParser.class -> Grammar.class
CoarseParser.class -> Rule.class
   edu.stanford.nlp.sempre.CoarseParser               -> edu.stanford.nlp.sempre.CoarseParser$CategorySpan  CoarseParser$CategorySpan.class
   edu.stanford.nlp.sempre.CoarseParser               -> edu.stanford.nlp.sempre.CoarseParser$CoarseParserState CoarseParser$CoarseParserState.class
   edu.stanford.nlp.sempre.CoarseParser               -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.CoarseParser               -> edu.stanford.nlp.sempre.Grammar                    Grammar.class
   edu.stanford.nlp.sempre.CoarseParser               -> edu.stanford.nlp.sempre.Rule                       Rule.class
ConcatFn$1.class -> ConcatFn.class
ConcatFn$1.class -> Derivation$Builder.class
ConcatFn$1.class -> Derivation.class
ConcatFn$1.class -> DerivationStream.class
ConcatFn$1.class -> Example.class
ConcatFn$1.class -> SemanticFn$Callable.class
ConcatFn$1.class -> SemanticFn.class
ConcatFn$1.class -> SingleDerivationStream.class
   edu.stanford.nlp.sempre.ConcatFn$1                 -> edu.stanford.nlp.sempre.ConcatFn                   ConcatFn.class
   edu.stanford.nlp.sempre.ConcatFn$1                 -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ConcatFn$1                 -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.ConcatFn$1                 -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.ConcatFn$1                 -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ConcatFn$1                 -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.ConcatFn$1                 -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.ConcatFn$1                 -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
ConcatFn.class -> ConcatFn$1.class
ConcatFn.class -> DerivationStream.class
ConcatFn.class -> Example.class
ConcatFn.class -> SemanticFn$Callable.class
ConcatFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.ConcatFn                   -> edu.stanford.nlp.sempre.ConcatFn$1                 ConcatFn$1.class
   edu.stanford.nlp.sempre.ConcatFn                   -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.ConcatFn                   -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ConcatFn                   -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.ConcatFn                   -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
ConstantFn$1.class -> ConstantFn.class
ConstantFn$1.class -> Derivation$Builder.class
ConstantFn$1.class -> Derivation.class
ConstantFn$1.class -> DerivationStream.class
ConstantFn$1.class -> Example.class
ConstantFn$1.class -> FeatureExtractor.class
ConstantFn$1.class -> Formula.class
ConstantFn$1.class -> SemType.class
ConstantFn$1.class -> SemanticFn$Callable.class
ConstantFn$1.class -> SemanticFn.class
ConstantFn$1.class -> SingleDerivationStream.class
   edu.stanford.nlp.sempre.ConstantFn$1               -> edu.stanford.nlp.sempre.ConstantFn                 ConstantFn.class
   edu.stanford.nlp.sempre.ConstantFn$1               -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ConstantFn$1               -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.ConstantFn$1               -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.ConstantFn$1               -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ConstantFn$1               -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.ConstantFn$1               -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.ConstantFn$1               -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.ConstantFn$1               -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.ConstantFn$1               -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.ConstantFn$1               -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
ConstantFn.class -> ConstantFn$1.class
ConstantFn.class -> DerivationStream.class
ConstantFn.class -> Example.class
ConstantFn.class -> Formula.class
ConstantFn.class -> Formulas.class
ConstantFn.class -> SemType.class
ConstantFn.class -> SemanticFn$Callable.class
ConstantFn.class -> SemanticFn.class
ConstantFn.class -> TypeInference.class
   edu.stanford.nlp.sempre.ConstantFn                 -> edu.stanford.nlp.sempre.ConstantFn$1               ConstantFn$1.class
   edu.stanford.nlp.sempre.ConstantFn                 -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.ConstantFn                 -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ConstantFn                 -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.ConstantFn                 -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.ConstantFn                 -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.ConstantFn                 -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.ConstantFn                 -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.ConstantFn                 -> edu.stanford.nlp.sempre.TypeInference              TypeInference.class
ContextFn$1.class -> ContextFn.class
ContextFn$1.class -> ContextValue$Exchange.class
ContextFn$1.class -> ContextValue.class
ContextFn$1.class -> Derivation$Builder.class
ContextFn$1.class -> Derivation.class
ContextFn$1.class -> DerivationStream.class
ContextFn$1.class -> Example.class
ContextFn$1.class -> Formula.class
ContextFn$1.class -> Formulas.class
ContextFn$1.class -> MultipleDerivationStream.class
ContextFn$1.class -> SemType.class
ContextFn$1.class -> SemanticFn$Callable.class
ContextFn$1.class -> SemanticFn.class
ContextFn$1.class -> TypeInference.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.ContextFn                  ContextFn.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.ContextValue$Exchange      ContextValue$Exchange.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.MultipleDerivationStream   MultipleDerivationStream.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.ContextFn$1                -> edu.stanford.nlp.sempre.TypeInference              TypeInference.class
ContextFn.class -> ContextFn$1.class
ContextFn.class -> DerivationStream.class
ContextFn.class -> Example.class
ContextFn.class -> SemType.class
ContextFn.class -> SemanticFn$Callable.class
ContextFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.ContextFn                  -> edu.stanford.nlp.sempre.ContextFn$1                ContextFn$1.class
   edu.stanford.nlp.sempre.ContextFn                  -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.ContextFn                  -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ContextFn                  -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.ContextFn                  -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.ContextFn                  -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
ContextValue$Exchange.class -> ContextValue.class
ContextValue$Exchange.class -> Formula.class
ContextValue$Exchange.class -> Formulas.class
ContextValue$Exchange.class -> Value.class
ContextValue$Exchange.class -> Values.class
   edu.stanford.nlp.sempre.ContextValue$Exchange      -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.ContextValue$Exchange      -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.ContextValue$Exchange      -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.ContextValue$Exchange      -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.ContextValue$Exchange      -> edu.stanford.nlp.sempre.Values                     Values.class
ContextValue.class -> ContextValue$Exchange.class
ContextValue.class -> DateValue.class
ContextValue.class -> KnowledgeGraph.class
ContextValue.class -> Value.class
   edu.stanford.nlp.sempre.ContextValue               -> edu.stanford.nlp.sempre.ContextValue$Exchange      ContextValue$Exchange.class
   edu.stanford.nlp.sempre.ContextValue               -> edu.stanford.nlp.sempre.DateValue                  DateValue.class
   edu.stanford.nlp.sempre.ContextValue               -> edu.stanford.nlp.sempre.KnowledgeGraph             KnowledgeGraph.class
   edu.stanford.nlp.sempre.ContextValue               -> edu.stanford.nlp.sempre.Value                      Value.class
Dataset$1.class -> Dataset.class
Dataset$1.class -> Example.class
   edu.stanford.nlp.sempre.Dataset$1                  -> edu.stanford.nlp.sempre.Dataset                    Dataset.class
   edu.stanford.nlp.sempre.Dataset$1                  -> edu.stanford.nlp.sempre.Example                    Example.class
Dataset$2.class -> Dataset.class
Dataset$2.class -> Example.class
   edu.stanford.nlp.sempre.Dataset$2                  -> edu.stanford.nlp.sempre.Dataset                    Dataset.class
   edu.stanford.nlp.sempre.Dataset$2                  -> edu.stanford.nlp.sempre.Example                    Example.class
Dataset$GroupInfo.class -> Dataset.class
Dataset$GroupInfo.class -> Example.class
   edu.stanford.nlp.sempre.Dataset$GroupInfo          -> edu.stanford.nlp.sempre.Dataset                    Dataset.class
   edu.stanford.nlp.sempre.Dataset$GroupInfo          -> edu.stanford.nlp.sempre.Example                    Example.class
Dataset$Options.class -> Dataset.class
   edu.stanford.nlp.sempre.Dataset$Options            -> edu.stanford.nlp.sempre.Dataset                    Dataset.class
Dataset.class -> ContextValue.class
Dataset.class -> Dataset$1.class
Dataset.class -> Dataset$2.class
Dataset.class -> Dataset$GroupInfo.class
Dataset.class -> Dataset$Options.class
Dataset.class -> Example$Builder.class
Dataset.class -> Example.class
Dataset.class -> Json.class
Dataset.class -> KnowledgeGraph.class
Dataset.class -> NaiveKnowledgeGraph.class
Dataset.class -> Value.class
   edu.stanford.nlp.sempre.Dataset                    -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.Dataset                    -> edu.stanford.nlp.sempre.Dataset$1                  Dataset$1.class
   edu.stanford.nlp.sempre.Dataset                    -> edu.stanford.nlp.sempre.Dataset$2                  Dataset$2.class
   edu.stanford.nlp.sempre.Dataset                    -> edu.stanford.nlp.sempre.Dataset$GroupInfo          Dataset$GroupInfo.class
   edu.stanford.nlp.sempre.Dataset                    -> edu.stanford.nlp.sempre.Dataset$Options            Dataset$Options.class
   edu.stanford.nlp.sempre.Dataset                    -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.Dataset                    -> edu.stanford.nlp.sempre.Example$Builder            Example$Builder.class
   edu.stanford.nlp.sempre.Dataset                    -> edu.stanford.nlp.sempre.Json                       Json.class
   edu.stanford.nlp.sempre.Dataset                    -> edu.stanford.nlp.sempre.KnowledgeGraph             KnowledgeGraph.class
   edu.stanford.nlp.sempre.Dataset                    -> edu.stanford.nlp.sempre.NaiveKnowledgeGraph        NaiveKnowledgeGraph.class
   edu.stanford.nlp.sempre.Dataset                    -> edu.stanford.nlp.sempre.Value                      Value.class
DateFn$1.class -> DateFn.class
DateFn$1.class -> DateValue.class
DateFn$1.class -> Derivation$Builder.class
DateFn$1.class -> Derivation.class
DateFn$1.class -> DerivationStream.class
DateFn$1.class -> Example.class
DateFn$1.class -> Formula.class
DateFn$1.class -> LanguageInfo.class
DateFn$1.class -> SemType.class
DateFn$1.class -> SemanticFn$Callable.class
DateFn$1.class -> SemanticFn.class
DateFn$1.class -> SingleDerivationStream.class
DateFn$1.class -> Value.class
DateFn$1.class -> ValueFormula.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.DateFn                     DateFn.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.DateValue                  DateValue.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.DateFn$1                   -> edu.stanford.nlp.sempre.ValueFormula               ValueFormula.class
DateFn.class -> DateFn$1.class
DateFn.class -> DerivationStream.class
DateFn.class -> Example.class
DateFn.class -> SemanticFn$Callable.class
DateFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.DateFn                     -> edu.stanford.nlp.sempre.DateFn$1                   DateFn$1.class
   edu.stanford.nlp.sempre.DateFn                     -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.DateFn                     -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.DateFn                     -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.DateFn                     -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
DateValue.class -> Value.class
   edu.stanford.nlp.sempre.DateValue                  -> edu.stanford.nlp.sempre.Value                      Value.class
DenotationFeatureMatcher.class -> FeatureMatcher.class
   edu.stanford.nlp.sempre.DenotationFeatureMatcher   -> edu.stanford.nlp.sempre.FeatureMatcher             FeatureMatcher.class
DerivInfo.class -> Formula.class
DerivInfo.class -> Rule.class
   edu.stanford.nlp.sempre.DerivInfo                  -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.DerivInfo                  -> edu.stanford.nlp.sempre.Rule                       Rule.class
DerivOpCountFeatureComputer$Options.class -> DerivOpCountFeatureComputer.class
   edu.stanford.nlp.sempre.DerivOpCountFeatureComputer$Options -> edu.stanford.nlp.sempre.DerivOpCountFeatureComputer DerivOpCountFeatureComputer.class
DerivOpCountFeatureComputer.class -> DerivOpCountFeatureComputer$Options.class
DerivOpCountFeatureComputer.class -> Derivation.class
DerivOpCountFeatureComputer.class -> Example.class
DerivOpCountFeatureComputer.class -> FeatureComputer.class
DerivOpCountFeatureComputer.class -> FeatureExtractor.class
DerivOpCountFeatureComputer.class -> Rule.class
DerivOpCountFeatureComputer.class -> SemanticFn.class
   edu.stanford.nlp.sempre.DerivOpCountFeatureComputer -> edu.stanford.nlp.sempre.DerivOpCountFeatureComputer$Options DerivOpCountFeatureComputer$Options.class
   edu.stanford.nlp.sempre.DerivOpCountFeatureComputer -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.DerivOpCountFeatureComputer -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.DerivOpCountFeatureComputer -> edu.stanford.nlp.sempre.FeatureComputer            FeatureComputer.class
   edu.stanford.nlp.sempre.DerivOpCountFeatureComputer -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.DerivOpCountFeatureComputer -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.DerivOpCountFeatureComputer -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
Derivation$Builder.class -> Derivation.class
Derivation$Builder.class -> FeatureVector.class
Derivation$Builder.class -> Formula.class
Derivation$Builder.class -> Rule.class
Derivation$Builder.class -> SemType.class
Derivation$Builder.class -> SemanticFn$Callable.class
Derivation$Builder.class -> SemanticFn.class
Derivation$Builder.class -> StringValue.class
Derivation$Builder.class -> Value.class
Derivation$Builder.class -> ValueFormula.class
   edu.stanford.nlp.sempre.Derivation$Builder         -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.Derivation$Builder         -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
   edu.stanford.nlp.sempre.Derivation$Builder         -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Derivation$Builder         -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.Derivation$Builder         -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.Derivation$Builder         -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.Derivation$Builder         -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.Derivation$Builder         -> edu.stanford.nlp.sempre.StringValue                StringValue.class
   edu.stanford.nlp.sempre.Derivation$Builder         -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.Derivation$Builder         -> edu.stanford.nlp.sempre.ValueFormula               ValueFormula.class
Derivation$CompatibilityDerivationComparator.class -> Derivation.class
   edu.stanford.nlp.sempre.Derivation$CompatibilityDerivationComparator -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
Derivation$Options.class -> Derivation.class
   edu.stanford.nlp.sempre.Derivation$Options         -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
Derivation$ScoredDerivationComparator.class -> Derivation.class
   edu.stanford.nlp.sempre.Derivation$ScoredDerivationComparator -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
Derivation.class -> AllFeatureMatcher.class
Derivation.class -> ContextValue.class
Derivation.class -> Derivation$Builder.class
Derivation.class -> Derivation$CompatibilityDerivationComparator.class
Derivation.class -> Derivation$Options.class
Derivation.class -> Derivation$ScoredDerivationComparator.class
Derivation.class -> ExactFeatureMatcher.class
Derivation.class -> Executor$Response.class
Derivation.class -> Executor.class
Derivation.class -> FeatureMatcher.class
Derivation.class -> FeatureVector.class
Derivation.class -> Formula.class
Derivation.class -> Formulas.class
Derivation.class -> HasScore.class
Derivation.class -> ListValue.class
Derivation.class -> Params.class
Derivation.class -> Rule.class
Derivation.class -> SemType.class
Derivation.class -> SemanticFn$Callable.class
Derivation.class -> SemanticFn.class
Derivation.class -> Value.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.AllFeatureMatcher          AllFeatureMatcher.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.Derivation$CompatibilityDerivationComparator Derivation$CompatibilityDerivationComparator.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.Derivation$Options         Derivation$Options.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.Derivation$ScoredDerivationComparator Derivation$ScoredDerivationComparator.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.ExactFeatureMatcher        ExactFeatureMatcher.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.Executor$Response          Executor$Response.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.FeatureMatcher             FeatureMatcher.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.HasScore                   HasScore.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.ListValue                  ListValue.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.Derivation                 -> edu.stanford.nlp.sempre.Value                      Value.class
DerivationPruner$Options.class -> DerivationPruner.class
   edu.stanford.nlp.sempre.DerivationPruner$Options   -> edu.stanford.nlp.sempre.DerivationPruner           DerivationPruner.class
DerivationPruner.class -> AggregateFormula.class
DerivationPruner.class -> ContextValue.class
DerivationPruner.class -> Derivation.class
DerivationPruner.class -> DerivationPruner$Options.class
DerivationPruner.class -> DerivationPruningComputer.class
DerivationPruner.class -> ErrorValue.class
DerivationPruner.class -> Example.class
DerivationPruner.class -> Executor$Response.class
DerivationPruner.class -> Executor.class
DerivationPruner.class -> Formula.class
DerivationPruner.class -> LambdaFormula.class
DerivationPruner.class -> ListValue.class
DerivationPruner.class -> MergeFormula.class
DerivationPruner.class -> Parser.class
DerivationPruner.class -> ParserState.class
DerivationPruner.class -> SemType.class
DerivationPruner.class -> SempreUtils.class
DerivationPruner.class -> SuperlativeFormula.class
DerivationPruner.class -> TypeInference.class
DerivationPruner.class -> Value.class
DerivationPruner.class -> ValueFormula.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.AggregateFormula           AggregateFormula.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.DerivationPruner$Options   DerivationPruner$Options.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.DerivationPruningComputer  DerivationPruningComputer.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.ErrorValue                 ErrorValue.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.Executor$Response          Executor$Response.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.LambdaFormula              LambdaFormula.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.ListValue                  ListValue.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.MergeFormula               MergeFormula.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.SempreUtils                SempreUtils.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.SuperlativeFormula         SuperlativeFormula.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.TypeInference              TypeInference.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.DerivationPruner           -> edu.stanford.nlp.sempre.ValueFormula               ValueFormula.class
DerivationPruningComputer.class -> Derivation.class
DerivationPruningComputer.class -> DerivationPruner.class
   edu.stanford.nlp.sempre.DerivationPruningComputer  -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.DerivationPruningComputer  -> edu.stanford.nlp.sempre.DerivationPruner           DerivationPruner.class
DerivationStream.class -> Derivation.class
   edu.stanford.nlp.sempre.DerivationStream           -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
DescriptionValue.class -> Value.class
   edu.stanford.nlp.sempre.DescriptionValue           -> edu.stanford.nlp.sempre.Value                      Value.class
ErrorValue.class -> BadFormulaException.class
ErrorValue.class -> Value.class
   edu.stanford.nlp.sempre.ErrorValue                 -> edu.stanford.nlp.sempre.BadFormulaException        BadFormulaException.class
   edu.stanford.nlp.sempre.ErrorValue                 -> edu.stanford.nlp.sempre.Value                      Value.class
ExactFeatureMatcher.class -> FeatureMatcher.class
   edu.stanford.nlp.sempre.ExactFeatureMatcher        -> edu.stanford.nlp.sempre.FeatureMatcher             FeatureMatcher.class
ExactValueEvaluator.class -> Value.class
ExactValueEvaluator.class -> ValueEvaluator.class
   edu.stanford.nlp.sempre.ExactValueEvaluator        -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.ExactValueEvaluator        -> edu.stanford.nlp.sempre.ValueEvaluator             ValueEvaluator.class
Example$Builder.class -> ContextValue.class
Example$Builder.class -> Derivation.class
Example$Builder.class -> Example.class
Example$Builder.class -> Formula.class
Example$Builder.class -> LanguageInfo.class
Example$Builder.class -> Value.class
   edu.stanford.nlp.sempre.Example$Builder            -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.Example$Builder            -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.Example$Builder            -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.Example$Builder            -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Example$Builder            -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.Example$Builder            -> edu.stanford.nlp.sempre.Value                      Value.class
Example.class -> ContextValue.class
Example.class -> Derivation$Builder.class
Example.class -> Derivation.class
Example.class -> Example$Builder.class
Example.class -> FeatureVector.class
Example.class -> Formula.class
Example.class -> Formulas.class
Example.class -> Json.class
Example.class -> LanguageAnalyzer.class
Example.class -> LanguageInfo.class
Example.class -> Rule.class
Example.class -> TargetValuePreprocessor.class
Example.class -> Value.class
Example.class -> Values.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.Example$Builder            Example$Builder.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.Json                       Json.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.LanguageAnalyzer           LanguageAnalyzer.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.TargetValuePreprocessor    TargetValuePreprocessor.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.Example                    -> edu.stanford.nlp.sempre.Values                     Values.class
ExampleUtils.class -> Dataset$Options.class
ExampleUtils.class -> Dataset.class
ExampleUtils.class -> Derivation.class
ExampleUtils.class -> Example.class
ExampleUtils.class -> Formula.class
ExampleUtils.class -> Value.class
   edu.stanford.nlp.sempre.ExampleUtils               -> edu.stanford.nlp.sempre.Dataset                    Dataset.class
   edu.stanford.nlp.sempre.ExampleUtils               -> edu.stanford.nlp.sempre.Dataset$Options            Dataset$Options.class
   edu.stanford.nlp.sempre.ExampleUtils               -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ExampleUtils               -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ExampleUtils               -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.ExampleUtils               -> edu.stanford.nlp.sempre.Value                      Value.class
Executor$Response.class -> Executor.class
Executor$Response.class -> Value.class
   edu.stanford.nlp.sempre.Executor$Response          -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.Executor$Response          -> edu.stanford.nlp.sempre.Value                      Value.class
Executor.class -> ContextValue.class
Executor.class -> Executor$Response.class
Executor.class -> Formula.class
   edu.stanford.nlp.sempre.Executor                   -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.Executor                   -> edu.stanford.nlp.sempre.Executor$Response          Executor$Response.class
   edu.stanford.nlp.sempre.Executor                   -> edu.stanford.nlp.sempre.Formula                    Formula.class
FeatureComputer.class -> Derivation.class
FeatureComputer.class -> Example.class
   edu.stanford.nlp.sempre.FeatureComputer            -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.FeatureComputer            -> edu.stanford.nlp.sempre.Example                    Example.class
FeatureExtractor$Options.class -> FeatureExtractor.class
   edu.stanford.nlp.sempre.FeatureExtractor$Options   -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
FeatureExtractor.class -> CanonicalNames.class
FeatureExtractor.class -> ContextValue.class
FeatureExtractor.class -> Derivation.class
FeatureExtractor.class -> ErrorValue.class
FeatureExtractor.class -> Example.class
FeatureExtractor.class -> Executor.class
FeatureExtractor.class -> FeatureComputer.class
FeatureExtractor.class -> FeatureExtractor$Options.class
FeatureExtractor.class -> Formula.class
FeatureExtractor.class -> Formulas.class
FeatureExtractor.class -> LanguageAnalyzer.class
FeatureExtractor.class -> LanguageInfo$DependencyEdge.class
FeatureExtractor.class -> LanguageInfo.class
FeatureExtractor.class -> ListValue.class
FeatureExtractor.class -> NumberValue.class
FeatureExtractor.class -> Rule.class
FeatureExtractor.class -> SemType.class
FeatureExtractor.class -> SemTypeHierarchy.class
FeatureExtractor.class -> SempreUtils.class
FeatureExtractor.class -> StringValue.class
FeatureExtractor.class -> Value.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.CanonicalNames             CanonicalNames.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.ErrorValue                 ErrorValue.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.FeatureComputer            FeatureComputer.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.FeatureExtractor$Options   FeatureExtractor$Options.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.LanguageAnalyzer           LanguageAnalyzer.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.LanguageInfo$DependencyEdge LanguageInfo$DependencyEdge.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.ListValue                  ListValue.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.NumberValue                NumberValue.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.SemTypeHierarchy           SemTypeHierarchy.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.SempreUtils                SempreUtils.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.StringValue                StringValue.class
   edu.stanford.nlp.sempre.FeatureExtractor           -> edu.stanford.nlp.sempre.Value                      Value.class
FeatureVector$Options.class -> FeatureVector.class
   edu.stanford.nlp.sempre.FeatureVector$Options      -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
FeatureVector.class -> AllFeatureMatcher.class
FeatureVector.class -> FeatureMatcher.class
FeatureVector.class -> FeatureVector$Options.class
FeatureVector.class -> Params.class
   edu.stanford.nlp.sempre.FeatureVector              -> edu.stanford.nlp.sempre.AllFeatureMatcher          AllFeatureMatcher.class
   edu.stanford.nlp.sempre.FeatureVector              -> edu.stanford.nlp.sempre.FeatureMatcher             FeatureMatcher.class
   edu.stanford.nlp.sempre.FeatureVector              -> edu.stanford.nlp.sempre.FeatureVector$Options      FeatureVector$Options.class
   edu.stanford.nlp.sempre.FeatureVector              -> edu.stanford.nlp.sempre.Params                     Params.class
FilterNerSpanFn$1.class -> Derivation$Builder.class
FilterNerSpanFn$1.class -> Derivation.class
FilterNerSpanFn$1.class -> DerivationStream.class
FilterNerSpanFn$1.class -> Example.class
FilterNerSpanFn$1.class -> FilterNerSpanFn.class
FilterNerSpanFn$1.class -> SemanticFn$Callable.class
FilterNerSpanFn$1.class -> SemanticFn.class
FilterNerSpanFn$1.class -> SingleDerivationStream.class
   edu.stanford.nlp.sempre.FilterNerSpanFn$1          -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.FilterNerSpanFn$1          -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.FilterNerSpanFn$1          -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.FilterNerSpanFn$1          -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FilterNerSpanFn$1          -> edu.stanford.nlp.sempre.FilterNerSpanFn            FilterNerSpanFn.class
   edu.stanford.nlp.sempre.FilterNerSpanFn$1          -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.FilterNerSpanFn$1          -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.FilterNerSpanFn$1          -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
FilterNerSpanFn.class -> DerivationStream.class
FilterNerSpanFn.class -> Example.class
FilterNerSpanFn.class -> FilterNerSpanFn$1.class
FilterNerSpanFn.class -> LanguageInfo.class
FilterNerSpanFn.class -> SemanticFn$Callable.class
FilterNerSpanFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.FilterNerSpanFn            -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.FilterNerSpanFn            -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FilterNerSpanFn            -> edu.stanford.nlp.sempre.FilterNerSpanFn$1          FilterNerSpanFn$1.class
   edu.stanford.nlp.sempre.FilterNerSpanFn            -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.FilterNerSpanFn            -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.FilterNerSpanFn            -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
FilterPosTagFn$1.class -> Derivation.class
FilterPosTagFn$1.class -> DerivationStream.class
FilterPosTagFn$1.class -> Example.class
FilterPosTagFn$1.class -> FilterPosTagFn.class
FilterPosTagFn$1.class -> SemanticFn$Callable.class
FilterPosTagFn$1.class -> SemanticFn.class
FilterPosTagFn$1.class -> SingleDerivationStream.class
   edu.stanford.nlp.sempre.FilterPosTagFn$1           -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.FilterPosTagFn$1           -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.FilterPosTagFn$1           -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FilterPosTagFn$1           -> edu.stanford.nlp.sempre.FilterPosTagFn             FilterPosTagFn.class
   edu.stanford.nlp.sempre.FilterPosTagFn$1           -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.FilterPosTagFn$1           -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.FilterPosTagFn$1           -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
FilterPosTagFn.class -> Derivation$Builder.class
FilterPosTagFn.class -> Derivation.class
FilterPosTagFn.class -> DerivationStream.class
FilterPosTagFn.class -> Example.class
FilterPosTagFn.class -> FilterPosTagFn$1.class
FilterPosTagFn.class -> SemanticFn$Callable.class
FilterPosTagFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.FilterPosTagFn             -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.FilterPosTagFn             -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.FilterPosTagFn             -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.FilterPosTagFn             -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FilterPosTagFn             -> edu.stanford.nlp.sempre.FilterPosTagFn$1           FilterPosTagFn$1.class
   edu.stanford.nlp.sempre.FilterPosTagFn             -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.FilterPosTagFn             -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
FilterSpanLengthFn$1.class -> Derivation$Builder.class
FilterSpanLengthFn$1.class -> Derivation.class
FilterSpanLengthFn$1.class -> DerivationStream.class
FilterSpanLengthFn$1.class -> Example.class
FilterSpanLengthFn$1.class -> FilterSpanLengthFn.class
FilterSpanLengthFn$1.class -> SemanticFn$Callable.class
FilterSpanLengthFn$1.class -> SemanticFn.class
FilterSpanLengthFn$1.class -> SingleDerivationStream.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn$1       -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn$1       -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn$1       -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn$1       -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn$1       -> edu.stanford.nlp.sempre.FilterSpanLengthFn         FilterSpanLengthFn.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn$1       -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn$1       -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn$1       -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
FilterSpanLengthFn.class -> DerivationStream.class
FilterSpanLengthFn.class -> Example.class
FilterSpanLengthFn.class -> FilterSpanLengthFn$1.class
FilterSpanLengthFn.class -> SemanticFn$Callable.class
FilterSpanLengthFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn         -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn         -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn         -> edu.stanford.nlp.sempre.FilterSpanLengthFn$1       FilterSpanLengthFn$1.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn         -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.FilterSpanLengthFn         -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
FilterTokenFn$1.class -> Derivation$Builder.class
FilterTokenFn$1.class -> Derivation.class
FilterTokenFn$1.class -> DerivationStream.class
FilterTokenFn$1.class -> Example.class
FilterTokenFn$1.class -> FilterTokenFn.class
FilterTokenFn$1.class -> SemanticFn$Callable.class
FilterTokenFn$1.class -> SemanticFn.class
FilterTokenFn$1.class -> SingleDerivationStream.class
   edu.stanford.nlp.sempre.FilterTokenFn$1            -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.FilterTokenFn$1            -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.FilterTokenFn$1            -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.FilterTokenFn$1            -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FilterTokenFn$1            -> edu.stanford.nlp.sempre.FilterTokenFn              FilterTokenFn.class
   edu.stanford.nlp.sempre.FilterTokenFn$1            -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.FilterTokenFn$1            -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.FilterTokenFn$1            -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
FilterTokenFn.class -> DerivationStream.class
FilterTokenFn.class -> Example.class
FilterTokenFn.class -> FilterTokenFn$1.class
FilterTokenFn.class -> SemanticFn$Callable.class
FilterTokenFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.FilterTokenFn              -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.FilterTokenFn              -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FilterTokenFn              -> edu.stanford.nlp.sempre.FilterTokenFn$1            FilterTokenFn$1.class
   edu.stanford.nlp.sempre.FilterTokenFn              -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.FilterTokenFn              -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
FloatingFeatureComputer.class -> Derivation.class
FloatingFeatureComputer.class -> Example.class
FloatingFeatureComputer.class -> FeatureComputer.class
FloatingFeatureComputer.class -> FeatureExtractor.class
FloatingFeatureComputer.class -> LanguageInfo.class
FloatingFeatureComputer.class -> Rule.class
   edu.stanford.nlp.sempre.FloatingFeatureComputer    -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.FloatingFeatureComputer    -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FloatingFeatureComputer    -> edu.stanford.nlp.sempre.FeatureComputer            FeatureComputer.class
   edu.stanford.nlp.sempre.FloatingFeatureComputer    -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.FloatingFeatureComputer    -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.FloatingFeatureComputer    -> edu.stanford.nlp.sempre.Rule                       Rule.class
FloatingParser$Options.class -> FloatingParser.class
   edu.stanford.nlp.sempre.FloatingParser$Options     -> edu.stanford.nlp.sempre.FloatingParser             FloatingParser.class
FloatingParser.class -> Example.class
FloatingParser.class -> FloatingParser$Options.class
FloatingParser.class -> FloatingParserState.class
FloatingParser.class -> Params.class
FloatingParser.class -> Parser$Spec.class
FloatingParser.class -> Parser.class
FloatingParser.class -> ParserState.class
   edu.stanford.nlp.sempre.FloatingParser             -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FloatingParser             -> edu.stanford.nlp.sempre.FloatingParser$Options     FloatingParser$Options.class
   edu.stanford.nlp.sempre.FloatingParser             -> edu.stanford.nlp.sempre.FloatingParserState        FloatingParserState.class
   edu.stanford.nlp.sempre.FloatingParser             -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.FloatingParser             -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.FloatingParser             -> edu.stanford.nlp.sempre.Parser$Spec                Parser$Spec.class
   edu.stanford.nlp.sempre.FloatingParser             -> edu.stanford.nlp.sempre.ParserState                ParserState.class
FloatingParserState.class -> ContextValue.class
FloatingParserState.class -> Derivation.class
FloatingParserState.class -> DerivationPruner.class
FloatingParserState.class -> DerivationStream.class
FloatingParserState.class -> ErrorValue.class
FloatingParserState.class -> Example.class
FloatingParserState.class -> Executor.class
FloatingParserState.class -> FloatingParser$Options.class
FloatingParserState.class -> FloatingParser.class
FloatingParserState.class -> FloatingRuleUtils.class
FloatingParserState.class -> Formula.class
FloatingParserState.class -> FuncSemType.class
FloatingParserState.class -> Grammar.class
FloatingParserState.class -> Params.class
FloatingParserState.class -> Parser$Options.class
FloatingParserState.class -> Parser.class
FloatingParserState.class -> ParserState.class
FloatingParserState.class -> Rule.class
FloatingParserState.class -> SemType.class
FloatingParserState.class -> SemanticFn$CallInfo.class
FloatingParserState.class -> SemanticFn$Callable.class
FloatingParserState.class -> SemanticFn.class
FloatingParserState.class -> Value.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.DerivationPruner           DerivationPruner.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.ErrorValue                 ErrorValue.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.FloatingParser             FloatingParser.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.FloatingParser$Options     FloatingParser$Options.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.FloatingRuleUtils          FloatingRuleUtils.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.FuncSemType                FuncSemType.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.Grammar                    Grammar.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.Parser$Options             Parser$Options.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.SemanticFn$CallInfo        SemanticFn$CallInfo.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.FloatingParserState        -> edu.stanford.nlp.sempre.Value                      Value.class
FloatingRuleUtils.class -> Derivation.class
FloatingRuleUtils.class -> Rule.class
   edu.stanford.nlp.sempre.FloatingRuleUtils          -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.FloatingRuleUtils          -> edu.stanford.nlp.sempre.Rule                       Rule.class
Formula$1.class -> Formula.class
Formula$1.class -> PrimitiveFormula.class
   edu.stanford.nlp.sempre.Formula$1                  -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Formula$1                  -> edu.stanford.nlp.sempre.PrimitiveFormula           PrimitiveFormula.class
Formula.class -> Formula$1.class
Formula.class -> Formulas.class
   edu.stanford.nlp.sempre.Formula                    -> edu.stanford.nlp.sempre.Formula$1                  Formula$1.class
   edu.stanford.nlp.sempre.Formula                    -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
FormulaMatchExecutor.class -> ContextValue.class
FormulaMatchExecutor.class -> Executor$Response.class
FormulaMatchExecutor.class -> Executor.class
FormulaMatchExecutor.class -> Formula.class
FormulaMatchExecutor.class -> Formulas.class
FormulaMatchExecutor.class -> StringValue.class
FormulaMatchExecutor.class -> Value.class
FormulaMatchExecutor.class -> ValueFormula.class
   edu.stanford.nlp.sempre.FormulaMatchExecutor       -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.FormulaMatchExecutor       -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.FormulaMatchExecutor       -> edu.stanford.nlp.sempre.Executor$Response          Executor$Response.class
   edu.stanford.nlp.sempre.FormulaMatchExecutor       -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.FormulaMatchExecutor       -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.FormulaMatchExecutor       -> edu.stanford.nlp.sempre.StringValue                StringValue.class
   edu.stanford.nlp.sempre.FormulaMatchExecutor       -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.FormulaMatchExecutor       -> edu.stanford.nlp.sempre.ValueFormula               ValueFormula.class
Formulas$1.class -> Formula.class
Formulas$1.class -> Formulas.class
Formulas$1.class -> LambdaFormula.class
Formulas$1.class -> VariableFormula.class
   edu.stanford.nlp.sempre.Formulas$1                 -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Formulas$1                 -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.Formulas$1                 -> edu.stanford.nlp.sempre.LambdaFormula              LambdaFormula.class
   edu.stanford.nlp.sempre.Formulas$1                 -> edu.stanford.nlp.sempre.VariableFormula            VariableFormula.class
Formulas$2.class -> Formula.class
Formulas$2.class -> Formulas.class
   edu.stanford.nlp.sempre.Formulas$2                 -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Formulas$2                 -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
Formulas$3.class -> Formula.class
Formulas$3.class -> Formulas.class
Formulas$3.class -> JoinFormula.class
Formulas$3.class -> LambdaFormula.class
   edu.stanford.nlp.sempre.Formulas$3                 -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Formulas$3                 -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.Formulas$3                 -> edu.stanford.nlp.sempre.JoinFormula                JoinFormula.class
   edu.stanford.nlp.sempre.Formulas$3                 -> edu.stanford.nlp.sempre.LambdaFormula              LambdaFormula.class
Formulas.class -> AggregateFormula$Mode.class
Formulas.class -> AggregateFormula.class
Formulas.class -> ArithmeticFormula$Mode.class
Formulas.class -> ArithmeticFormula.class
Formulas.class -> CallFormula.class
Formulas.class -> CanonicalNames.class
Formulas.class -> Formula.class
Formulas.class -> Formulas$1.class
Formulas.class -> Formulas$2.class
Formulas.class -> Formulas$3.class
Formulas.class -> JoinFormula.class
Formulas.class -> LambdaFormula.class
Formulas.class -> MarkFormula.class
Formulas.class -> MergeFormula$Mode.class
Formulas.class -> MergeFormula.class
Formulas.class -> NameValue.class
Formulas.class -> NotFormula.class
Formulas.class -> NumberValue.class
Formulas.class -> PrimitiveFormula.class
Formulas.class -> ReverseFormula.class
Formulas.class -> StringValue.class
Formulas.class -> SuperlativeFormula$Mode.class
Formulas.class -> SuperlativeFormula.class
Formulas.class -> Value.class
Formulas.class -> ValueFormula.class
Formulas.class -> Values.class
Formulas.class -> VariableFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.AggregateFormula           AggregateFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.AggregateFormula$Mode      AggregateFormula$Mode.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.ArithmeticFormula          ArithmeticFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.ArithmeticFormula$Mode     ArithmeticFormula$Mode.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.CallFormula                CallFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.CanonicalNames             CanonicalNames.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.Formulas$1                 Formulas$1.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.Formulas$2                 Formulas$2.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.Formulas$3                 Formulas$3.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.JoinFormula                JoinFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.LambdaFormula              LambdaFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.MarkFormula                MarkFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.MergeFormula               MergeFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.MergeFormula$Mode          MergeFormula$Mode.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.NameValue                  NameValue.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.NotFormula                 NotFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.NumberValue                NumberValue.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.PrimitiveFormula           PrimitiveFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.ReverseFormula             ReverseFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.StringValue                StringValue.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.SuperlativeFormula         SuperlativeFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.SuperlativeFormula$Mode    SuperlativeFormula$Mode.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.ValueFormula               ValueFormula.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.Values                     Values.class
   edu.stanford.nlp.sempre.Formulas                   -> edu.stanford.nlp.sempre.VariableFormula            VariableFormula.class
FuncSemType.class -> AtomicSemType.class
FuncSemType.class -> SemType.class
FuncSemType.class -> TopSemType.class
   edu.stanford.nlp.sempre.FuncSemType                -> edu.stanford.nlp.sempre.AtomicSemType              AtomicSemType.class
   edu.stanford.nlp.sempre.FuncSemType                -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.FuncSemType                -> edu.stanford.nlp.sempre.TopSemType                 TopSemType.class
FuzzyMatchFn$FuzzyMatchFnMode.class -> FuzzyMatchFn.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$FuzzyMatchFnMode -> edu.stanford.nlp.sempre.FuzzyMatchFn               FuzzyMatchFn.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> ContextValue.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> Derivation$Builder.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> Derivation.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> Example.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> FeatureExtractor.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> FeatureVector.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> Formula.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> FuzzyMatchFn$FuzzyMatchFnMode.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> FuzzyMatchFn$Options.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> FuzzyMatchFn.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> KnowledgeGraph.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> MultipleDerivationStream.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> SemType.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> SemanticFn$Callable.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> SemanticFn.class
FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class -> TypeInference.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.FuzzyMatchFn               FuzzyMatchFn.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.FuzzyMatchFn$FuzzyMatchFnMode FuzzyMatchFn$FuzzyMatchFnMode.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.FuzzyMatchFn$Options       FuzzyMatchFn$Options.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.KnowledgeGraph             KnowledgeGraph.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.MultipleDerivationStream   MultipleDerivationStream.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs -> edu.stanford.nlp.sempre.TypeInference              TypeInference.class
FuzzyMatchFn$Options.class -> FuzzyMatchFn.class
   edu.stanford.nlp.sempre.FuzzyMatchFn$Options       -> edu.stanford.nlp.sempre.FuzzyMatchFn               FuzzyMatchFn.class
FuzzyMatchFn.class -> DerivationStream.class
FuzzyMatchFn.class -> Example.class
FuzzyMatchFn.class -> FuzzyMatchFn$FuzzyMatchFnMode.class
FuzzyMatchFn.class -> FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class
FuzzyMatchFn.class -> FuzzyMatchFn$Options.class
FuzzyMatchFn.class -> SemanticFn$Callable.class
FuzzyMatchFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.FuzzyMatchFn               -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.FuzzyMatchFn               -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.FuzzyMatchFn               -> edu.stanford.nlp.sempre.FuzzyMatchFn$FuzzyMatchFnMode FuzzyMatchFn$FuzzyMatchFnMode.class
   edu.stanford.nlp.sempre.FuzzyMatchFn               -> edu.stanford.nlp.sempre.FuzzyMatchFn$LazyFuzzyMatchFnDerivs FuzzyMatchFn$LazyFuzzyMatchFnDerivs.class
   edu.stanford.nlp.sempre.FuzzyMatchFn               -> edu.stanford.nlp.sempre.FuzzyMatchFn$Options       FuzzyMatchFn$Options.class
   edu.stanford.nlp.sempre.FuzzyMatchFn               -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.FuzzyMatchFn               -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
Grammar$Options.class -> Grammar.class
   edu.stanford.nlp.sempre.Grammar$Options            -> edu.stanford.nlp.sempre.Grammar                    Grammar.class
Grammar.class -> ConstantFn.class
Grammar.class -> Formula.class
Grammar.class -> Grammar$Options.class
Grammar.class -> JoinFn.class
Grammar.class -> Rule.class
Grammar.class -> SelectFn.class
Grammar.class -> SemanticFn.class
Grammar.class -> SempreUtils.class
   edu.stanford.nlp.sempre.Grammar                    -> edu.stanford.nlp.sempre.ConstantFn                 ConstantFn.class
   edu.stanford.nlp.sempre.Grammar                    -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Grammar                    -> edu.stanford.nlp.sempre.Grammar$Options            Grammar$Options.class
   edu.stanford.nlp.sempre.Grammar                    -> edu.stanford.nlp.sempre.JoinFn                     JoinFn.class
   edu.stanford.nlp.sempre.Grammar                    -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.Grammar                    -> edu.stanford.nlp.sempre.SelectFn                   SelectFn.class
   edu.stanford.nlp.sempre.Grammar                    -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.Grammar                    -> edu.stanford.nlp.sempre.SempreUtils                SempreUtils.class
IdentityFn$1.class -> Derivation$Builder.class
IdentityFn$1.class -> Derivation.class
IdentityFn$1.class -> DerivationStream.class
IdentityFn$1.class -> Example.class
IdentityFn$1.class -> IdentityFn.class
IdentityFn$1.class -> SemanticFn$Callable.class
IdentityFn$1.class -> SemanticFn.class
IdentityFn$1.class -> SingleDerivationStream.class
   edu.stanford.nlp.sempre.IdentityFn$1               -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.IdentityFn$1               -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.IdentityFn$1               -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.IdentityFn$1               -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.IdentityFn$1               -> edu.stanford.nlp.sempre.IdentityFn                 IdentityFn.class
   edu.stanford.nlp.sempre.IdentityFn$1               -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.IdentityFn$1               -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.IdentityFn$1               -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
IdentityFn.class -> DerivationStream.class
IdentityFn.class -> Example.class
IdentityFn.class -> IdentityFn$1.class
IdentityFn.class -> SemanticFn$Callable.class
IdentityFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.IdentityFn                 -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.IdentityFn                 -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.IdentityFn                 -> edu.stanford.nlp.sempre.IdentityFn$1               IdentityFn$1.class
   edu.stanford.nlp.sempre.IdentityFn                 -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.IdentityFn                 -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
IdentityTargetValuePreprocessor.class -> TargetValuePreprocessor.class
IdentityTargetValuePreprocessor.class -> Value.class
   edu.stanford.nlp.sempre.IdentityTargetValuePreprocessor -> edu.stanford.nlp.sempre.TargetValuePreprocessor    TargetValuePreprocessor.class
   edu.stanford.nlp.sempre.IdentityTargetValuePreprocessor -> edu.stanford.nlp.sempre.Value                      Value.class
JavaExecutor$BasicFunctions.class -> Formula.class
JavaExecutor$BasicFunctions.class -> Formulas.class
JavaExecutor$BasicFunctions.class -> JavaExecutor.class
JavaExecutor$BasicFunctions.class -> LambdaFormula.class
JavaExecutor$BasicFunctions.class -> NameValue.class
JavaExecutor$BasicFunctions.class -> StringValue.class
JavaExecutor$BasicFunctions.class -> Value.class
JavaExecutor$BasicFunctions.class -> ValueFormula.class
   edu.stanford.nlp.sempre.JavaExecutor$BasicFunctions -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.JavaExecutor$BasicFunctions -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.JavaExecutor$BasicFunctions -> edu.stanford.nlp.sempre.JavaExecutor               JavaExecutor.class
   edu.stanford.nlp.sempre.JavaExecutor$BasicFunctions -> edu.stanford.nlp.sempre.LambdaFormula              LambdaFormula.class
   edu.stanford.nlp.sempre.JavaExecutor$BasicFunctions -> edu.stanford.nlp.sempre.NameValue                  NameValue.class
   edu.stanford.nlp.sempre.JavaExecutor$BasicFunctions -> edu.stanford.nlp.sempre.StringValue                StringValue.class
   edu.stanford.nlp.sempre.JavaExecutor$BasicFunctions -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.JavaExecutor$BasicFunctions -> edu.stanford.nlp.sempre.ValueFormula               ValueFormula.class
JavaExecutor$Options.class -> JavaExecutor.class
   edu.stanford.nlp.sempre.JavaExecutor$Options       -> edu.stanford.nlp.sempre.JavaExecutor               JavaExecutor.class
JavaExecutor.class -> BooleanValue.class
JavaExecutor.class -> CallFormula.class
JavaExecutor.class -> ContextValue.class
JavaExecutor.class -> ErrorValue.class
JavaExecutor.class -> Executor$Response.class
JavaExecutor.class -> Executor.class
JavaExecutor.class -> Formula.class
JavaExecutor.class -> Formulas.class
JavaExecutor.class -> JavaExecutor$BasicFunctions.class
JavaExecutor.class -> JavaExecutor$Options.class
JavaExecutor.class -> ListValue.class
JavaExecutor.class -> NameValue.class
JavaExecutor.class -> NumberValue.class
JavaExecutor.class -> StringValue.class
JavaExecutor.class -> Value.class
JavaExecutor.class -> ValueFormula.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.BooleanValue               BooleanValue.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.CallFormula                CallFormula.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.ErrorValue                 ErrorValue.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.Executor$Response          Executor$Response.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.JavaExecutor$BasicFunctions JavaExecutor$BasicFunctions.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.JavaExecutor$Options       JavaExecutor$Options.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.ListValue                  ListValue.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.NameValue                  NameValue.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.NumberValue                NumberValue.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.StringValue                StringValue.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.JavaExecutor               -> edu.stanford.nlp.sempre.ValueFormula               ValueFormula.class
JoinFn$LazyJoinFnDerivs.class -> AtomicSemType.class
JoinFn$LazyJoinFnDerivs.class -> ConstantFn.class
JoinFn$LazyJoinFnDerivs.class -> Derivation$Builder.class
JoinFn$LazyJoinFnDerivs.class -> Derivation.class
JoinFn$LazyJoinFnDerivs.class -> DerivationStream.class
JoinFn$LazyJoinFnDerivs.class -> Example.class
JoinFn$LazyJoinFnDerivs.class -> FeatureExtractor.class
JoinFn$LazyJoinFnDerivs.class -> FeatureVector.class
JoinFn$LazyJoinFnDerivs.class -> Formula.class
JoinFn$LazyJoinFnDerivs.class -> Formulas.class
JoinFn$LazyJoinFnDerivs.class -> JoinFn$Options.class
JoinFn$LazyJoinFnDerivs.class -> JoinFn.class
JoinFn$LazyJoinFnDerivs.class -> JoinFormula.class
JoinFn$LazyJoinFnDerivs.class -> LambdaFormula.class
JoinFn$LazyJoinFnDerivs.class -> LanguageInfo.class
JoinFn$LazyJoinFnDerivs.class -> MultipleDerivationStream.class
JoinFn$LazyJoinFnDerivs.class -> SemType.class
JoinFn$LazyJoinFnDerivs.class -> SemTypeHierarchy.class
JoinFn$LazyJoinFnDerivs.class -> SemanticFn$CallInfo.class
JoinFn$LazyJoinFnDerivs.class -> SemanticFn$Callable.class
JoinFn$LazyJoinFnDerivs.class -> SemanticFn$Options.class
JoinFn$LazyJoinFnDerivs.class -> SemanticFn.class
JoinFn$LazyJoinFnDerivs.class -> TopSemType.class
JoinFn$LazyJoinFnDerivs.class -> TypeInference.class
JoinFn$LazyJoinFnDerivs.class -> UnionSemType.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.AtomicSemType              AtomicSemType.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.ConstantFn                 ConstantFn.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.JoinFn                     JoinFn.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.JoinFn$Options             JoinFn$Options.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.JoinFormula                JoinFormula.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.LambdaFormula              LambdaFormula.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.MultipleDerivationStream   MultipleDerivationStream.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.SemTypeHierarchy           SemTypeHierarchy.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.SemanticFn$CallInfo        SemanticFn$CallInfo.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.SemanticFn$Options         SemanticFn$Options.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.TopSemType                 TopSemType.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.TypeInference              TypeInference.class
   edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    -> edu.stanford.nlp.sempre.UnionSemType               UnionSemType.class
JoinFn$Options.class -> JoinFn.class
   edu.stanford.nlp.sempre.JoinFn$Options             -> edu.stanford.nlp.sempre.JoinFn                     JoinFn.class
JoinFn.class -> ConstantFn.class
JoinFn.class -> DerivationStream.class
JoinFn.class -> Example.class
JoinFn.class -> JoinFn$LazyJoinFnDerivs.class
JoinFn.class -> JoinFn$Options.class
JoinFn.class -> SemanticFn$Callable.class
JoinFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.JoinFn                     -> edu.stanford.nlp.sempre.ConstantFn                 ConstantFn.class
   edu.stanford.nlp.sempre.JoinFn                     -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.JoinFn                     -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.JoinFn                     -> edu.stanford.nlp.sempre.JoinFn$LazyJoinFnDerivs    JoinFn$LazyJoinFnDerivs.class
   edu.stanford.nlp.sempre.JoinFn                     -> edu.stanford.nlp.sempre.JoinFn$Options             JoinFn$Options.class
   edu.stanford.nlp.sempre.JoinFn                     -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.JoinFn                     -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
JoinFormula.class -> Formula.class
JoinFormula.class -> Formulas.class
JoinFormula.class -> ValueFormula.class
   edu.stanford.nlp.sempre.JoinFormula                -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.JoinFormula                -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.JoinFormula                -> edu.stanford.nlp.sempre.ValueFormula               ValueFormula.class
KnowledgeGraph.class -> BadFormulaException.class
KnowledgeGraph.class -> Formula.class
KnowledgeGraph.class -> FuzzyMatchFn$FuzzyMatchFnMode.class
KnowledgeGraph.class -> FuzzyMatchFn.class
KnowledgeGraph.class -> NaiveKnowledgeGraph.class
KnowledgeGraph.class -> NameValue.class
KnowledgeGraph.class -> SempreUtils.class
KnowledgeGraph.class -> Value.class
   edu.stanford.nlp.sempre.KnowledgeGraph             -> edu.stanford.nlp.sempre.BadFormulaException        BadFormulaException.class
   edu.stanford.nlp.sempre.KnowledgeGraph             -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.KnowledgeGraph             -> edu.stanford.nlp.sempre.FuzzyMatchFn               FuzzyMatchFn.class
   edu.stanford.nlp.sempre.KnowledgeGraph             -> edu.stanford.nlp.sempre.FuzzyMatchFn$FuzzyMatchFnMode FuzzyMatchFn$FuzzyMatchFnMode.class
   edu.stanford.nlp.sempre.KnowledgeGraph             -> edu.stanford.nlp.sempre.NaiveKnowledgeGraph        NaiveKnowledgeGraph.class
   edu.stanford.nlp.sempre.KnowledgeGraph             -> edu.stanford.nlp.sempre.NameValue                  NameValue.class
   edu.stanford.nlp.sempre.KnowledgeGraph             -> edu.stanford.nlp.sempre.SempreUtils                SempreUtils.class
   edu.stanford.nlp.sempre.KnowledgeGraph             -> edu.stanford.nlp.sempre.Value                      Value.class
LambdaFormula.class -> Formula.class
   edu.stanford.nlp.sempre.LambdaFormula              -> edu.stanford.nlp.sempre.Formula                    Formula.class
LanguageAnalyzer$Options.class -> LanguageAnalyzer.class
   edu.stanford.nlp.sempre.LanguageAnalyzer$Options   -> edu.stanford.nlp.sempre.LanguageAnalyzer           LanguageAnalyzer.class
LanguageAnalyzer.class -> LanguageAnalyzer$Options.class
LanguageAnalyzer.class -> LanguageInfo.class
LanguageAnalyzer.class -> SempreUtils.class
   edu.stanford.nlp.sempre.LanguageAnalyzer           -> edu.stanford.nlp.sempre.LanguageAnalyzer$Options   LanguageAnalyzer$Options.class
   edu.stanford.nlp.sempre.LanguageAnalyzer           -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.LanguageAnalyzer           -> edu.stanford.nlp.sempre.SempreUtils                SempreUtils.class
LanguageInfo$DependencyEdge.class -> LanguageInfo.class
   edu.stanford.nlp.sempre.LanguageInfo$DependencyEdge -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
LanguageInfo$LanguageUtils.class -> LanguageInfo$WordInfo.class
LanguageInfo$LanguageUtils.class -> LanguageInfo.class
   edu.stanford.nlp.sempre.LanguageInfo$LanguageUtils -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.LanguageInfo$LanguageUtils -> edu.stanford.nlp.sempre.LanguageInfo$WordInfo      LanguageInfo$WordInfo.class
LanguageInfo$WordInfo.class -> LanguageInfo.class
   edu.stanford.nlp.sempre.LanguageInfo$WordInfo      -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
LanguageInfo.class -> LanguageInfo$DependencyEdge.class
LanguageInfo.class -> LanguageInfo$LanguageUtils.class
LanguageInfo.class -> LanguageInfo$WordInfo.class
   edu.stanford.nlp.sempre.LanguageInfo               -> edu.stanford.nlp.sempre.LanguageInfo$DependencyEdge LanguageInfo$DependencyEdge.class
   edu.stanford.nlp.sempre.LanguageInfo               -> edu.stanford.nlp.sempre.LanguageInfo$LanguageUtils LanguageInfo$LanguageUtils.class
   edu.stanford.nlp.sempre.LanguageInfo               -> edu.stanford.nlp.sempre.LanguageInfo$WordInfo      LanguageInfo$WordInfo.class
Learner$Options.class -> Learner.class
   edu.stanford.nlp.sempre.Learner$Options            -> edu.stanford.nlp.sempre.Learner                    Learner.class
Learner.class -> Builder$Options.class
Learner.class -> Builder.class
Learner.class -> Dataset.class
Learner.class -> Derivation.class
Learner.class -> Example.class
Learner.class -> ExampleUtils.class
Learner.class -> Formula.class
Learner.class -> Grammar.class
Learner.class -> Learner$Options.class
Learner.class -> Params.class
Learner.class -> Parser.class
Learner.class -> ParserState.class
Learner.class -> Rule.class
Learner.class -> SemanticFn.class
Learner.class -> SempreUtils.class
Learner.class -> Value.class
Learner.class -> ValueEvaluator.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Builder                    Builder.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Builder$Options            Builder$Options.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Dataset                    Dataset.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.ExampleUtils               ExampleUtils.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Grammar                    Grammar.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Learner$Options            Learner$Options.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.SempreUtils                SempreUtils.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.Learner                    -> edu.stanford.nlp.sempre.ValueEvaluator             ValueEvaluator.class
ListParserAgenda.class -> ParserAgenda.class
ListParserAgenda.class -> PrioritizedDerivationStream.class
   edu.stanford.nlp.sempre.ListParserAgenda           -> edu.stanford.nlp.sempre.ParserAgenda               ParserAgenda.class
   edu.stanford.nlp.sempre.ListParserAgenda           -> edu.stanford.nlp.sempre.PrioritizedDerivationStream PrioritizedDerivationStream.class
ListValue.class -> Value.class
ListValue.class -> Values.class
   edu.stanford.nlp.sempre.ListValue                  -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.ListValue                  -> edu.stanford.nlp.sempre.Values                     Values.class
Main.class -> Builder.class
Main.class -> Dataset.class
Main.class -> Learner.class
Main.class -> Master.class
Main.class -> Params.class
Main.class -> Parser.class
Main.class -> Server.class
   edu.stanford.nlp.sempre.Main                       -> edu.stanford.nlp.sempre.Builder                    Builder.class
   edu.stanford.nlp.sempre.Main                       -> edu.stanford.nlp.sempre.Dataset                    Dataset.class
   edu.stanford.nlp.sempre.Main                       -> edu.stanford.nlp.sempre.Learner                    Learner.class
   edu.stanford.nlp.sempre.Main                       -> edu.stanford.nlp.sempre.Master                     Master.class
   edu.stanford.nlp.sempre.Main                       -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.Main                       -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.Main                       -> edu.stanford.nlp.sempre.Server                     Server.class
MarkFormula.class -> Formula.class
   edu.stanford.nlp.sempre.MarkFormula                -> edu.stanford.nlp.sempre.Formula                    Formula.class
Master$Options.class -> Master.class
   edu.stanford.nlp.sempre.Master$Options             -> edu.stanford.nlp.sempre.Master                     Master.class
Master$Response.class -> Builder.class
Master$Response.class -> ContextValue.class
Master$Response.class -> Derivation.class
Master$Response.class -> Example.class
Master$Response.class -> Executor.class
Master$Response.class -> Formula.class
Master$Response.class -> Master.class
Master$Response.class -> Value.class
   edu.stanford.nlp.sempre.Master$Response            -> edu.stanford.nlp.sempre.Builder                    Builder.class
   edu.stanford.nlp.sempre.Master$Response            -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.Master$Response            -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.Master$Response            -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.Master$Response            -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.Master$Response            -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Master$Response            -> edu.stanford.nlp.sempre.Master                     Master.class
   edu.stanford.nlp.sempre.Master$Response            -> edu.stanford.nlp.sempre.Value                      Value.class
Master.class -> Builder.class
Master.class -> ContextValue.class
Master.class -> Dataset.class
Master.class -> DateValue.class
Master.class -> Derivation.class
Master.class -> Example$Builder.class
Master.class -> Example.class
Master.class -> Executor$Response.class
Master.class -> Executor.class
Master.class -> FeatureVector.class
Master.class -> Formula.class
Master.class -> Formulas.class
Master.class -> Grammar.class
Master.class -> KnowledgeGraph.class
Master.class -> Learner.class
Master.class -> Master$Options.class
Master.class -> Master$Response.class
Master.class -> NaiveKnowledgeGraph.class
Master.class -> Params.class
Master.class -> Parser.class
Master.class -> ParserState.class
Master.class -> Rule.class
Master.class -> SemType.class
Master.class -> Session.class
Master.class -> TypeInference.class
Master.class -> Value.class
Master.class -> Values.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Builder                    Builder.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Dataset                    Dataset.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.DateValue                  DateValue.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Example$Builder            Example$Builder.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Executor$Response          Executor$Response.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Grammar                    Grammar.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.KnowledgeGraph             KnowledgeGraph.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Learner                    Learner.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Master$Options             Master$Options.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Master$Response            Master$Response.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.NaiveKnowledgeGraph        NaiveKnowledgeGraph.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Session                    Session.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.TypeInference              TypeInference.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.Master                     -> edu.stanford.nlp.sempre.Values                     Values.class
MergeFn$1.class -> Derivation$Builder.class
MergeFn$1.class -> Derivation.class
MergeFn$1.class -> DerivationStream.class
MergeFn$1.class -> Example.class
MergeFn$1.class -> FeatureVector.class
MergeFn$1.class -> Formula.class
MergeFn$1.class -> MergeFn$Options.class
MergeFn$1.class -> MergeFn.class
MergeFn$1.class -> MergeFormula$Mode.class
MergeFn$1.class -> MergeFormula.class
MergeFn$1.class -> SemType.class
MergeFn$1.class -> SemanticFn$Callable.class
MergeFn$1.class -> SemanticFn$Options.class
MergeFn$1.class -> SemanticFn.class
MergeFn$1.class -> SingleDerivationStream.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.MergeFn                    MergeFn.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.MergeFn$Options            MergeFn$Options.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.MergeFormula               MergeFormula.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.MergeFormula$Mode          MergeFormula$Mode.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.SemanticFn$Options         SemanticFn$Options.class
   edu.stanford.nlp.sempre.MergeFn$1                  -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
MergeFn$Options.class -> MergeFn.class
   edu.stanford.nlp.sempre.MergeFn$Options            -> edu.stanford.nlp.sempre.MergeFn                    MergeFn.class
MergeFn.class -> DerivationStream.class
MergeFn.class -> Example.class
MergeFn.class -> Formula.class
MergeFn.class -> Formulas.class
MergeFn.class -> MergeFn$1.class
MergeFn.class -> MergeFn$Options.class
MergeFn.class -> MergeFormula$Mode.class
MergeFn.class -> MergeFormula.class
MergeFn.class -> SemanticFn$Callable.class
MergeFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.MergeFn                    -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.MergeFn                    -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.MergeFn                    -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.MergeFn                    -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.MergeFn                    -> edu.stanford.nlp.sempre.MergeFn$1                  MergeFn$1.class
   edu.stanford.nlp.sempre.MergeFn                    -> edu.stanford.nlp.sempre.MergeFn$Options            MergeFn$Options.class
   edu.stanford.nlp.sempre.MergeFn                    -> edu.stanford.nlp.sempre.MergeFormula               MergeFormula.class
   edu.stanford.nlp.sempre.MergeFn                    -> edu.stanford.nlp.sempre.MergeFormula$Mode          MergeFormula$Mode.class
   edu.stanford.nlp.sempre.MergeFn                    -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.MergeFn                    -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
MergeFormula$Mode.class -> MergeFormula.class
   edu.stanford.nlp.sempre.MergeFormula$Mode          -> edu.stanford.nlp.sempre.MergeFormula               MergeFormula.class
MergeFormula.class -> Formula.class
MergeFormula.class -> MergeFormula$Mode.class
   edu.stanford.nlp.sempre.MergeFormula               -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.MergeFormula               -> edu.stanford.nlp.sempre.MergeFormula$Mode          MergeFormula$Mode.class
MultipleDerivationStream.class -> Derivation.class
MultipleDerivationStream.class -> DerivationStream.class
MultipleDerivationStream.class -> FeatureExtractor.class
MultipleDerivationStream.class -> Rule.class
MultipleDerivationStream.class -> SemanticFn.class
   edu.stanford.nlp.sempre.MultipleDerivationStream   -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.MultipleDerivationStream   -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.MultipleDerivationStream   -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.MultipleDerivationStream   -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.MultipleDerivationStream   -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
NaiveKnowledgeGraph$KnowledgeGraphTriple.class -> NaiveKnowledgeGraph.class
NaiveKnowledgeGraph$KnowledgeGraphTriple.class -> NameValue.class
NaiveKnowledgeGraph$KnowledgeGraphTriple.class -> StringValue.class
NaiveKnowledgeGraph$KnowledgeGraphTriple.class -> Value.class
NaiveKnowledgeGraph$KnowledgeGraphTriple.class -> Values.class
   edu.stanford.nlp.sempre.NaiveKnowledgeGraph$KnowledgeGraphTriple -> edu.stanford.nlp.sempre.NaiveKnowledgeGraph        NaiveKnowledgeGraph.class
   edu.stanford.nlp.sempre.NaiveKnowledgeGraph$KnowledgeGraphTriple -> edu.stanford.nlp.sempre.NameValue                  NameValue.class
   edu.stanford.nlp.sempre.NaiveKnowledgeGraph$KnowledgeGraphTriple -> edu.stanford.nlp.sempre.StringValue                StringValue.class
   edu.stanford.nlp.sempre.NaiveKnowledgeGraph$KnowledgeGraphTriple -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.NaiveKnowledgeGraph$KnowledgeGraphTriple -> edu.stanford.nlp.sempre.Values                     Values.class
NaiveKnowledgeGraph.class -> Formula.class
NaiveKnowledgeGraph.class -> FuzzyMatchFn$FuzzyMatchFnMode.class
NaiveKnowledgeGraph.class -> FuzzyMatchFn.class
NaiveKnowledgeGraph.class -> KnowledgeGraph.class
NaiveKnowledgeGraph.class -> NaiveKnowledgeGraph$KnowledgeGraphTriple.class
NaiveKnowledgeGraph.class -> Value.class
   edu.stanford.nlp.sempre.NaiveKnowledgeGraph        -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.NaiveKnowledgeGraph        -> edu.stanford.nlp.sempre.FuzzyMatchFn               FuzzyMatchFn.class
   edu.stanford.nlp.sempre.NaiveKnowledgeGraph        -> edu.stanford.nlp.sempre.FuzzyMatchFn$FuzzyMatchFnMode FuzzyMatchFn$FuzzyMatchFnMode.class
   edu.stanford.nlp.sempre.NaiveKnowledgeGraph        -> edu.stanford.nlp.sempre.KnowledgeGraph             KnowledgeGraph.class
   edu.stanford.nlp.sempre.NaiveKnowledgeGraph        -> edu.stanford.nlp.sempre.NaiveKnowledgeGraph$KnowledgeGraphTriple NaiveKnowledgeGraph$KnowledgeGraphTriple.class
   edu.stanford.nlp.sempre.NaiveKnowledgeGraph        -> edu.stanford.nlp.sempre.Value                      Value.class
NameValue.class -> Value.class
   edu.stanford.nlp.sempre.NameValue                  -> edu.stanford.nlp.sempre.Value                      Value.class
NotFormula.class -> Formula.class
   edu.stanford.nlp.sempre.NotFormula                 -> edu.stanford.nlp.sempre.Formula                    Formula.class
NullExecutor.class -> ContextValue.class
NullExecutor.class -> Executor$Response.class
NullExecutor.class -> Executor.class
NullExecutor.class -> Formula.class
NullExecutor.class -> Value.class
   edu.stanford.nlp.sempre.NullExecutor               -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.NullExecutor               -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.NullExecutor               -> edu.stanford.nlp.sempre.Executor$Response          Executor$Response.class
   edu.stanford.nlp.sempre.NullExecutor               -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.NullExecutor               -> edu.stanford.nlp.sempre.Value                      Value.class
NullTypeLookup.class -> SemType.class
NullTypeLookup.class -> TypeLookup.class
   edu.stanford.nlp.sempre.NullTypeLookup             -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.NullTypeLookup             -> edu.stanford.nlp.sempre.TypeLookup                 TypeLookup.class
NumberFn$1.class -> Derivation$Builder.class
NumberFn$1.class -> Derivation.class
NumberFn$1.class -> DerivationStream.class
NumberFn$1.class -> Example.class
NumberFn$1.class -> Formula.class
NumberFn$1.class -> LanguageInfo.class
NumberFn$1.class -> NumberFn$Options.class
NumberFn$1.class -> NumberFn.class
NumberFn$1.class -> NumberValue.class
NumberFn$1.class -> SemType.class
NumberFn$1.class -> SemanticFn$Callable.class
NumberFn$1.class -> SemanticFn.class
NumberFn$1.class -> SingleDerivationStream.class
NumberFn$1.class -> Value.class
NumberFn$1.class -> ValueFormula.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.NumberFn                   NumberFn.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.NumberFn$Options           NumberFn$Options.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.NumberValue                NumberValue.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.NumberFn$1                 -> edu.stanford.nlp.sempre.ValueFormula               ValueFormula.class
NumberFn$Options.class -> NumberFn.class
   edu.stanford.nlp.sempre.NumberFn$Options           -> edu.stanford.nlp.sempre.NumberFn                   NumberFn.class
NumberFn.class -> DerivationStream.class
NumberFn.class -> Example.class
NumberFn.class -> NumberFn$1.class
NumberFn.class -> NumberFn$Options.class
NumberFn.class -> SemanticFn$Callable.class
NumberFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.NumberFn                   -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.NumberFn                   -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.NumberFn                   -> edu.stanford.nlp.sempre.NumberFn$1                 NumberFn$1.class
   edu.stanford.nlp.sempre.NumberFn                   -> edu.stanford.nlp.sempre.NumberFn$Options           NumberFn$Options.class
   edu.stanford.nlp.sempre.NumberFn                   -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.NumberFn                   -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
NumberValue.class -> Value.class
   edu.stanford.nlp.sempre.NumberValue                -> edu.stanford.nlp.sempre.Value                      Value.class
Params$L1Reg.class -> Params.class
   edu.stanford.nlp.sempre.Params$L1Reg               -> edu.stanford.nlp.sempre.Params                     Params.class
Params$Options.class -> Params.class
   edu.stanford.nlp.sempre.Params$Options             -> edu.stanford.nlp.sempre.Params                     Params.class
Params.class -> Params$L1Reg.class
Params.class -> Params$Options.class
   edu.stanford.nlp.sempre.Params                     -> edu.stanford.nlp.sempre.Params$L1Reg               Params$L1Reg.class
   edu.stanford.nlp.sempre.Params                     -> edu.stanford.nlp.sempre.Params$Options             Params$Options.class
Parser$Options.class -> Parser.class
   edu.stanford.nlp.sempre.Parser$Options             -> edu.stanford.nlp.sempre.Parser                     Parser.class
Parser$Spec.class -> Executor.class
Parser$Spec.class -> FeatureExtractor.class
Parser$Spec.class -> Grammar.class
Parser$Spec.class -> Parser.class
Parser$Spec.class -> ValueEvaluator.class
   edu.stanford.nlp.sempre.Parser$Spec                -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.Parser$Spec                -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.Parser$Spec                -> edu.stanford.nlp.sempre.Grammar                    Grammar.class
   edu.stanford.nlp.sempre.Parser$Spec                -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.Parser$Spec                -> edu.stanford.nlp.sempre.ValueEvaluator             ValueEvaluator.class
Parser.class -> ContextValue.class
Parser.class -> Derivation.class
Parser.class -> Example.class
Parser.class -> Executor$Response.class
Parser.class -> Executor.class
Parser.class -> FeatureExtractor.class
Parser.class -> FeatureVector.class
Parser.class -> Formula.class
Parser.class -> Grammar.class
Parser.class -> Params.class
Parser.class -> Parser$Options.class
Parser.class -> Parser$Spec.class
Parser.class -> ParserState.class
Parser.class -> Rule.class
Parser.class -> Value.class
Parser.class -> ValueEvaluator.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.Executor$Response          Executor$Response.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.Grammar                    Grammar.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.Parser$Options             Parser$Options.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.Parser$Spec                Parser$Spec.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.Parser                     -> edu.stanford.nlp.sempre.ValueEvaluator             ValueEvaluator.class
ParserState$1.class -> ParserState$CustomExpectedCount.class
ParserState$1.class -> ParserState.class
   edu.stanford.nlp.sempre.ParserState$1              -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.ParserState$1              -> edu.stanford.nlp.sempre.ParserState$CustomExpectedCount ParserState$CustomExpectedCount.class
ParserState$CustomExpectedCount.class -> ParserState.class
   edu.stanford.nlp.sempre.ParserState$CustomExpectedCount -> edu.stanford.nlp.sempre.ParserState                ParserState.class
ParserState$Options.class -> ParserState$CustomExpectedCount.class
ParserState$Options.class -> ParserState.class
   edu.stanford.nlp.sempre.ParserState$Options        -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.ParserState$Options        -> edu.stanford.nlp.sempre.ParserState$CustomExpectedCount ParserState$CustomExpectedCount.class
ParserState.class -> ChartParserState.class
ParserState.class -> ContextValue.class
ParserState.class -> Derivation$Builder.class
ParserState.class -> Derivation.class
ParserState.class -> Example.class
ParserState.class -> Executor.class
ParserState.class -> FeatureExtractor.class
ParserState.class -> Formula.class
ParserState.class -> Params.class
ParserState.class -> Parser$Options.class
ParserState.class -> Parser.class
ParserState.class -> ParserState$1.class
ParserState.class -> ParserState$CustomExpectedCount.class
ParserState.class -> ParserState$Options.class
ParserState.class -> Rule.class
ParserState.class -> Value.class
ParserState.class -> ValueEvaluator.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.ChartParserState           ChartParserState.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.Parser$Options             Parser$Options.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.ParserState$1              ParserState$1.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.ParserState$CustomExpectedCount ParserState$CustomExpectedCount.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.ParserState$Options        ParserState$Options.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.ParserState                -> edu.stanford.nlp.sempre.ValueEvaluator             ValueEvaluator.class
PrimitiveFormula.class -> Formula.class
   edu.stanford.nlp.sempre.PrimitiveFormula           -> edu.stanford.nlp.sempre.Formula                    Formula.class
PrioritizedDerivationStream.class -> Derivation.class
PrioritizedDerivationStream.class -> DerivationStream.class
PrioritizedDerivationStream.class -> HasScore.class
   edu.stanford.nlp.sempre.PrioritizedDerivationStream -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.PrioritizedDerivationStream -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.PrioritizedDerivationStream -> edu.stanford.nlp.sempre.HasScore                   HasScore.class
QueueParserAgenda.class -> ParserAgenda.class
QueueParserAgenda.class -> PrioritizedDerivationStream.class
   edu.stanford.nlp.sempre.QueueParserAgenda          -> edu.stanford.nlp.sempre.ParserAgenda               ParserAgenda.class
   edu.stanford.nlp.sempre.QueueParserAgenda          -> edu.stanford.nlp.sempre.PrioritizedDerivationStream PrioritizedDerivationStream.class
ReinforcementParser$Options.class -> ReinforcementParser.class
   edu.stanford.nlp.sempre.ReinforcementParser$Options -> edu.stanford.nlp.sempre.ReinforcementParser        ReinforcementParser.class
ReinforcementParser.class -> CoarseParser.class
ReinforcementParser.class -> Example.class
ReinforcementParser.class -> Grammar.class
ReinforcementParser.class -> Params.class
ReinforcementParser.class -> Parser$Options.class
ReinforcementParser.class -> Parser$Spec.class
ReinforcementParser.class -> Parser.class
ReinforcementParser.class -> ParserState.class
ReinforcementParser.class -> ReinforcementParser$Options.class
ReinforcementParser.class -> ReinforcementParserState$StateBuilder.class
ReinforcementParser.class -> ReinforcementParserState.class
ReinforcementParser.class -> Rule.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.CoarseParser               CoarseParser.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.Grammar                    Grammar.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.Parser$Options             Parser$Options.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.Parser$Spec                Parser$Spec.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.ReinforcementParser$Options ReinforcementParser$Options.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.ReinforcementParserState   ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.ReinforcementParserState$StateBuilder ReinforcementParserState$StateBuilder.class
   edu.stanford.nlp.sempre.ReinforcementParser        -> edu.stanford.nlp.sempre.Rule                       Rule.class
ReinforcementParserState$1.class -> ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$1 -> edu.stanford.nlp.sempre.ReinforcementParserState   ReinforcementParserState.class
ReinforcementParserState$AgendaSampler.class -> Derivation.class
ReinforcementParserState$AgendaSampler.class -> ParserAgenda.class
ReinforcementParserState$AgendaSampler.class -> PrioritizedDerivationStream.class
ReinforcementParserState$AgendaSampler.class -> ReinforcementParserState$Sampler.class
ReinforcementParserState$AgendaSampler.class -> ReinforcementParserState.class
ReinforcementParserState$AgendaSampler.class -> ReinforcementUtils.class
   edu.stanford.nlp.sempre.ReinforcementParserState$AgendaSampler -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ReinforcementParserState$AgendaSampler -> edu.stanford.nlp.sempre.ParserAgenda               ParserAgenda.class
   edu.stanford.nlp.sempre.ReinforcementParserState$AgendaSampler -> edu.stanford.nlp.sempre.PrioritizedDerivationStream PrioritizedDerivationStream.class
   edu.stanford.nlp.sempre.ReinforcementParserState$AgendaSampler -> edu.stanford.nlp.sempre.ReinforcementParserState   ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$AgendaSampler -> edu.stanford.nlp.sempre.ReinforcementParserState$Sampler ReinforcementParserState$Sampler.class
   edu.stanford.nlp.sempre.ReinforcementParserState$AgendaSampler -> edu.stanford.nlp.sempre.ReinforcementUtils         ReinforcementUtils.class
ReinforcementParserState$CorrectDerivationComparator.class -> Derivation.class
ReinforcementParserState$CorrectDerivationComparator.class -> JoinFn.class
ReinforcementParserState$CorrectDerivationComparator.class -> ReinforcementParserState.class
ReinforcementParserState$CorrectDerivationComparator.class -> Rule.class
ReinforcementParserState$CorrectDerivationComparator.class -> SemanticFn.class
   edu.stanford.nlp.sempre.ReinforcementParserState$CorrectDerivationComparator -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ReinforcementParserState$CorrectDerivationComparator -> edu.stanford.nlp.sempre.JoinFn                     JoinFn.class
   edu.stanford.nlp.sempre.ReinforcementParserState$CorrectDerivationComparator -> edu.stanford.nlp.sempre.ReinforcementParserState   ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$CorrectDerivationComparator -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.ReinforcementParserState$CorrectDerivationComparator -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
ReinforcementParserState$MaxSampler.class -> Derivation.class
ReinforcementParserState$MaxSampler.class -> ParserAgenda.class
ReinforcementParserState$MaxSampler.class -> PrioritizedDerivationStream.class
ReinforcementParserState$MaxSampler.class -> ReinforcementParserState$Sampler.class
ReinforcementParserState$MaxSampler.class -> ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MaxSampler -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MaxSampler -> edu.stanford.nlp.sempre.ParserAgenda               ParserAgenda.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MaxSampler -> edu.stanford.nlp.sempre.PrioritizedDerivationStream PrioritizedDerivationStream.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MaxSampler -> edu.stanford.nlp.sempre.ReinforcementParserState   ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MaxSampler -> edu.stanford.nlp.sempre.ReinforcementParserState$Sampler ReinforcementParserState$Sampler.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> DerivInfo.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> Derivation.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> DerivationStream.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> Formula.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> ParserAgenda.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> PrioritizedDerivationStream.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> ReinforcementParser$Options.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> ReinforcementParser.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> ReinforcementParserState$OracleInfo.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> ReinforcementParserState$Sampler.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> ReinforcementParserState.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> ReinforcementUtils.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> Rule.class
ReinforcementParserState$MultiplicativeProposalSampler.class -> SingleDerivationStream.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.DerivInfo                  DerivInfo.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.ParserAgenda               ParserAgenda.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.PrioritizedDerivationStream PrioritizedDerivationStream.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.ReinforcementParser        ReinforcementParser.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.ReinforcementParser$Options ReinforcementParser$Options.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.ReinforcementParserState   ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.ReinforcementParserState$OracleInfo ReinforcementParserState$OracleInfo.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.ReinforcementParserState$Sampler ReinforcementParserState$Sampler.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.ReinforcementUtils         ReinforcementUtils.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
ReinforcementParserState$NecessaryDeriv.class -> ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$NecessaryDeriv -> edu.stanford.nlp.sempre.ReinforcementParserState   ReinforcementParserState.class
ReinforcementParserState$OracleInfo.class -> DerivInfo.class
ReinforcementParserState$OracleInfo.class -> Derivation.class
ReinforcementParserState$OracleInfo.class -> Formula.class
ReinforcementParserState$OracleInfo.class -> ReinforcementParser.class
ReinforcementParserState$OracleInfo.class -> ReinforcementParserState$CorrectDerivationComparator.class
ReinforcementParserState$OracleInfo.class -> ReinforcementParserState$NecessaryDeriv.class
ReinforcementParserState$OracleInfo.class -> ReinforcementParserState.class
ReinforcementParserState$OracleInfo.class -> Rule.class
   edu.stanford.nlp.sempre.ReinforcementParserState$OracleInfo -> edu.stanford.nlp.sempre.DerivInfo                  DerivInfo.class
   edu.stanford.nlp.sempre.ReinforcementParserState$OracleInfo -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ReinforcementParserState$OracleInfo -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.ReinforcementParserState$OracleInfo -> edu.stanford.nlp.sempre.ReinforcementParser        ReinforcementParser.class
   edu.stanford.nlp.sempre.ReinforcementParserState$OracleInfo -> edu.stanford.nlp.sempre.ReinforcementParserState   ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$OracleInfo -> edu.stanford.nlp.sempre.ReinforcementParserState$CorrectDerivationComparator ReinforcementParserState$CorrectDerivationComparator.class
   edu.stanford.nlp.sempre.ReinforcementParserState$OracleInfo -> edu.stanford.nlp.sempre.ReinforcementParserState$NecessaryDeriv ReinforcementParserState$NecessaryDeriv.class
   edu.stanford.nlp.sempre.ReinforcementParserState$OracleInfo -> edu.stanford.nlp.sempre.Rule                       Rule.class
ReinforcementParserState$Sampler.class -> Derivation.class
ReinforcementParserState$Sampler.class -> DerivationStream.class
ReinforcementParserState$Sampler.class -> ParserAgenda.class
ReinforcementParserState$Sampler.class -> PrioritizedDerivationStream.class
ReinforcementParserState$Sampler.class -> ReinforcementParser.class
ReinforcementParserState$Sampler.class -> ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$Sampler -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ReinforcementParserState$Sampler -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.ReinforcementParserState$Sampler -> edu.stanford.nlp.sempre.ParserAgenda               ParserAgenda.class
   edu.stanford.nlp.sempre.ReinforcementParserState$Sampler -> edu.stanford.nlp.sempre.PrioritizedDerivationStream PrioritizedDerivationStream.class
   edu.stanford.nlp.sempre.ReinforcementParserState$Sampler -> edu.stanford.nlp.sempre.ReinforcementParser        ReinforcementParser.class
   edu.stanford.nlp.sempre.ReinforcementParserState$Sampler -> edu.stanford.nlp.sempre.ReinforcementParserState   ReinforcementParserState.class
ReinforcementParserState$StateBuilder.class -> Example.class
ReinforcementParserState$StateBuilder.class -> Params.class
ReinforcementParserState$StateBuilder.class -> ParserState.class
ReinforcementParserState$StateBuilder.class -> ReinforcementParser.class
ReinforcementParserState$StateBuilder.class -> ReinforcementParserState$1.class
ReinforcementParserState$StateBuilder.class -> ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$StateBuilder -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ReinforcementParserState$StateBuilder -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.ReinforcementParserState$StateBuilder -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$StateBuilder -> edu.stanford.nlp.sempre.ReinforcementParser        ReinforcementParser.class
   edu.stanford.nlp.sempre.ReinforcementParserState$StateBuilder -> edu.stanford.nlp.sempre.ReinforcementParserState   ReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState$StateBuilder -> edu.stanford.nlp.sempre.ReinforcementParserState$1 ReinforcementParserState$1.class
ReinforcementParserState.class -> AbstractReinforcementParserState.class
ReinforcementParserState.class -> ChartParserState$ChartFillingData.class
ReinforcementParserState.class -> ChartParserState.class
ReinforcementParserState.class -> CoarseParser$CoarseParserState.class
ReinforcementParserState.class -> CoarseParser.class
ReinforcementParserState.class -> ContextValue.class
ReinforcementParserState.class -> Derivation.class
ReinforcementParserState.class -> DerivationStream.class
ReinforcementParserState.class -> Example.class
ReinforcementParserState.class -> Executor.class
ReinforcementParserState.class -> FeatureExtractor.class
ReinforcementParserState.class -> FeatureVector.class
ReinforcementParserState.class -> Formula.class
ReinforcementParserState.class -> Json.class
ReinforcementParserState.class -> ListParserAgenda.class
ReinforcementParserState.class -> Params.class
ReinforcementParserState.class -> Parser$Options.class
ReinforcementParserState.class -> Parser.class
ReinforcementParserState.class -> ParserAgenda.class
ReinforcementParserState.class -> ParserState.class
ReinforcementParserState.class -> PrioritizedDerivationStream.class
ReinforcementParserState.class -> QueueParserAgenda.class
ReinforcementParserState.class -> ReinforcementParser$Options.class
ReinforcementParserState.class -> ReinforcementParser.class
ReinforcementParserState.class -> ReinforcementParserState$1.class
ReinforcementParserState.class -> ReinforcementParserState$AgendaSampler.class
ReinforcementParserState.class -> ReinforcementParserState$CorrectDerivationComparator.class
ReinforcementParserState.class -> ReinforcementParserState$MaxSampler.class
ReinforcementParserState.class -> ReinforcementParserState$MultiplicativeProposalSampler.class
ReinforcementParserState.class -> ReinforcementParserState$NecessaryDeriv.class
ReinforcementParserState.class -> ReinforcementParserState$OracleInfo.class
ReinforcementParserState.class -> ReinforcementParserState$Sampler.class
ReinforcementParserState.class -> ReinforcementParserState$StateBuilder.class
ReinforcementParserState.class -> ReinforcementUtils.class
ReinforcementParserState.class -> Rule.class
ReinforcementParserState.class -> SempreUtils.class
ReinforcementParserState.class -> SingleDerivationStream.class
ReinforcementParserState.class -> Value.class
ReinforcementParserState.class -> ValueEvaluator.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.AbstractReinforcementParserState AbstractReinforcementParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ChartParserState           ChartParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ChartParserState$ChartFillingData ChartParserState$ChartFillingData.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.CoarseParser               CoarseParser.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.CoarseParser$CoarseParserState CoarseParser$CoarseParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.Executor                   Executor.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.Json                       Json.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ListParserAgenda           ListParserAgenda.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.Parser                     Parser.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.Parser$Options             Parser$Options.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ParserAgenda               ParserAgenda.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ParserState                ParserState.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.PrioritizedDerivationStream PrioritizedDerivationStream.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.QueueParserAgenda          QueueParserAgenda.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementParser        ReinforcementParser.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementParser$Options ReinforcementParser$Options.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementParserState$1 ReinforcementParserState$1.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementParserState$AgendaSampler ReinforcementParserState$AgendaSampler.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementParserState$CorrectDerivationComparator ReinforcementParserState$CorrectDerivationComparator.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementParserState$MaxSampler ReinforcementParserState$MaxSampler.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementParserState$MultiplicativeProposalSampler ReinforcementParserState$MultiplicativeProposalSampler.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementParserState$NecessaryDeriv ReinforcementParserState$NecessaryDeriv.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementParserState$OracleInfo ReinforcementParserState$OracleInfo.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementParserState$Sampler ReinforcementParserState$Sampler.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementParserState$StateBuilder ReinforcementParserState$StateBuilder.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ReinforcementUtils         ReinforcementUtils.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.SempreUtils                SempreUtils.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.ReinforcementParserState   -> edu.stanford.nlp.sempre.ValueEvaluator             ValueEvaluator.class
ReinforcementUtils.class -> HasScore.class
ReinforcementUtils.class -> ParserAgenda.class
   edu.stanford.nlp.sempre.ReinforcementUtils         -> edu.stanford.nlp.sempre.HasScore                   HasScore.class
   edu.stanford.nlp.sempre.ReinforcementUtils         -> edu.stanford.nlp.sempre.ParserAgenda               ParserAgenda.class
ReverseFormula.class -> Formula.class
   edu.stanford.nlp.sempre.ReverseFormula             -> edu.stanford.nlp.sempre.Formula                    Formula.class
Rule.class -> FloatingParser$Options.class
Rule.class -> FloatingParser.class
Rule.class -> SemanticFn.class
   edu.stanford.nlp.sempre.Rule                       -> edu.stanford.nlp.sempre.FloatingParser             FloatingParser.class
   edu.stanford.nlp.sempre.Rule                       -> edu.stanford.nlp.sempre.FloatingParser$Options     FloatingParser$Options.class
   edu.stanford.nlp.sempre.Rule                       -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
SelectFn$1.class -> Derivation$Builder.class
SelectFn$1.class -> Derivation.class
SelectFn$1.class -> DerivationStream.class
SelectFn$1.class -> Example.class
SelectFn$1.class -> FeatureExtractor.class
SelectFn$1.class -> FeatureVector.class
SelectFn$1.class -> LanguageInfo.class
SelectFn$1.class -> SelectFn$Options.class
SelectFn$1.class -> SelectFn.class
SelectFn$1.class -> SemanticFn$Callable.class
SelectFn$1.class -> SemanticFn.class
SelectFn$1.class -> SingleDerivationStream.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.SelectFn                   SelectFn.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.SelectFn$Options           SelectFn$Options.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.SelectFn$1                 -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
SelectFn$Options.class -> SelectFn.class
   edu.stanford.nlp.sempre.SelectFn$Options           -> edu.stanford.nlp.sempre.SelectFn                   SelectFn.class
SelectFn.class -> DerivationStream.class
SelectFn.class -> Example.class
SelectFn.class -> SelectFn$1.class
SelectFn.class -> SelectFn$Options.class
SelectFn.class -> SemanticFn$Callable.class
SelectFn.class -> SemanticFn.class
   edu.stanford.nlp.sempre.SelectFn                   -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.SelectFn                   -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.SelectFn                   -> edu.stanford.nlp.sempre.SelectFn$1                 SelectFn$1.class
   edu.stanford.nlp.sempre.SelectFn                   -> edu.stanford.nlp.sempre.SelectFn$Options           SelectFn$Options.class
   edu.stanford.nlp.sempre.SelectFn                   -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.SelectFn                   -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
SemType.class -> AtomicSemType.class
SemType.class -> CanonicalNames.class
SemType.class -> FuncSemType.class
SemType.class -> TopSemType.class
SemType.class -> UnionSemType.class
   edu.stanford.nlp.sempre.SemType                    -> edu.stanford.nlp.sempre.AtomicSemType              AtomicSemType.class
   edu.stanford.nlp.sempre.SemType                    -> edu.stanford.nlp.sempre.CanonicalNames             CanonicalNames.class
   edu.stanford.nlp.sempre.SemType                    -> edu.stanford.nlp.sempre.FuncSemType                FuncSemType.class
   edu.stanford.nlp.sempre.SemType                    -> edu.stanford.nlp.sempre.TopSemType                 TopSemType.class
   edu.stanford.nlp.sempre.SemType                    -> edu.stanford.nlp.sempre.UnionSemType               UnionSemType.class
SemTypeHierarchy$Options.class -> SemTypeHierarchy.class
   edu.stanford.nlp.sempre.SemTypeHierarchy$Options   -> edu.stanford.nlp.sempre.SemTypeHierarchy           SemTypeHierarchy.class
SemTypeHierarchy.class -> CanonicalNames.class
SemTypeHierarchy.class -> SemTypeHierarchy$Options.class
   edu.stanford.nlp.sempre.SemTypeHierarchy           -> edu.stanford.nlp.sempre.CanonicalNames             CanonicalNames.class
   edu.stanford.nlp.sempre.SemTypeHierarchy           -> edu.stanford.nlp.sempre.SemTypeHierarchy$Options   SemTypeHierarchy$Options.class
SemanticFn$CallInfo.class -> Derivation.class
SemanticFn$CallInfo.class -> Formula.class
SemanticFn$CallInfo.class -> Formulas.class
SemanticFn$CallInfo.class -> Rule.class
SemanticFn$CallInfo.class -> SemanticFn$Callable.class
SemanticFn$CallInfo.class -> SemanticFn.class
   edu.stanford.nlp.sempre.SemanticFn$CallInfo        -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.SemanticFn$CallInfo        -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.SemanticFn$CallInfo        -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.SemanticFn$CallInfo        -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.SemanticFn$CallInfo        -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.SemanticFn$CallInfo        -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
SemanticFn$Callable.class -> Derivation.class
SemanticFn$Callable.class -> Rule.class
SemanticFn$Callable.class -> SemanticFn.class
   edu.stanford.nlp.sempre.SemanticFn$Callable        -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.SemanticFn$Callable        -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.SemanticFn$Callable        -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
SemanticFn$Options.class -> SemanticFn.class
   edu.stanford.nlp.sempre.SemanticFn$Options         -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
SemanticFn.class -> DerivationStream.class
SemanticFn.class -> Example.class
SemanticFn.class -> Params.class
SemanticFn.class -> SemanticFn$CallInfo.class
SemanticFn.class -> SemanticFn$Callable.class
SemanticFn.class -> SemanticFn$Options.class
   edu.stanford.nlp.sempre.SemanticFn                 -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.SemanticFn                 -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.SemanticFn                 -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.SemanticFn                 -> edu.stanford.nlp.sempre.SemanticFn$CallInfo        SemanticFn$CallInfo.class
   edu.stanford.nlp.sempre.SemanticFn                 -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.SemanticFn                 -> edu.stanford.nlp.sempre.SemanticFn$Options         SemanticFn$Options.class
Server$ExchangeState$CandidatePredicates.class -> Formula.class
Server$ExchangeState$CandidatePredicates.class -> Server$ExchangeState.class
Server$ExchangeState$CandidatePredicates.class -> Server.class
   edu.stanford.nlp.sempre.Server$ExchangeState$CandidatePredicates -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Server$ExchangeState$CandidatePredicates -> edu.stanford.nlp.sempre.Server                     Server.class
   edu.stanford.nlp.sempre.Server$ExchangeState$CandidatePredicates -> edu.stanford.nlp.sempre.Server$ExchangeState       Server$ExchangeState.class
Server$ExchangeState.class -> ContextValue$Exchange.class
Server$ExchangeState.class -> ContextValue.class
Server$ExchangeState.class -> DateValue.class
Server$ExchangeState.class -> Derivation.class
Server$ExchangeState.class -> Example.class
Server$ExchangeState.class -> Formula.class
Server$ExchangeState.class -> Json.class
Server$ExchangeState.class -> LanguageInfo.class
Server$ExchangeState.class -> Master$Response.class
Server$ExchangeState.class -> Master.class
Server$ExchangeState.class -> NameValue.class
Server$ExchangeState.class -> NumberValue.class
Server$ExchangeState.class -> Params.class
Server$ExchangeState.class -> Rule.class
Server$ExchangeState.class -> SecureIdentifiers.class
Server$ExchangeState.class -> SemanticFn.class
Server$ExchangeState.class -> Server$ExchangeState$CandidatePredicates.class
Server$ExchangeState.class -> Server$Options.class
Server$ExchangeState.class -> Server.class
Server$ExchangeState.class -> Session.class
Server$ExchangeState.class -> StringValue.class
Server$ExchangeState.class -> TableValue.class
Server$ExchangeState.class -> UriValue.class
Server$ExchangeState.class -> Value.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.ContextValue$Exchange      ContextValue$Exchange.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.DateValue                  DateValue.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Json                       Json.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Master                     Master.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Master$Response            Master$Response.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.NameValue                  NameValue.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.NumberValue                NumberValue.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Params                     Params.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Rule                       Rule.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.SecureIdentifiers          SecureIdentifiers.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Server                     Server.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Server$ExchangeState$CandidatePredicates Server$ExchangeState$CandidatePredicates.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Server$Options             Server$Options.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Session                    Session.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.StringValue                StringValue.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.TableValue                 TableValue.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.UriValue                   UriValue.class
   edu.stanford.nlp.sempre.Server$ExchangeState       -> edu.stanford.nlp.sempre.Value                      Value.class
Server$Handler.class -> Server$ExchangeState.class
Server$Handler.class -> Server.class
   edu.stanford.nlp.sempre.Server$Handler             -> edu.stanford.nlp.sempre.Server                     Server.class
   edu.stanford.nlp.sempre.Server$Handler             -> edu.stanford.nlp.sempre.Server$ExchangeState       Server$ExchangeState.class
Server$Options.class -> Server.class
   edu.stanford.nlp.sempre.Server$Options             -> edu.stanford.nlp.sempre.Server                     Server.class
Server.class -> Master.class
Server.class -> Server$ExchangeState.class
Server.class -> Server$Handler.class
Server.class -> Server$Options.class
   edu.stanford.nlp.sempre.Server                     -> edu.stanford.nlp.sempre.Master                     Master.class
   edu.stanford.nlp.sempre.Server                     -> edu.stanford.nlp.sempre.Server$ExchangeState       Server$ExchangeState.class
   edu.stanford.nlp.sempre.Server                     -> edu.stanford.nlp.sempre.Server$Handler             Server$Handler.class
   edu.stanford.nlp.sempre.Server                     -> edu.stanford.nlp.sempre.Server$Options             Server$Options.class
Session.class -> ContextValue$Exchange.class
Session.class -> ContextValue.class
Session.class -> DateValue.class
Session.class -> Derivation.class
Session.class -> Example.class
Session.class -> Formula.class
Session.class -> Value.class
   edu.stanford.nlp.sempre.Session                    -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.Session                    -> edu.stanford.nlp.sempre.ContextValue$Exchange      ContextValue$Exchange.class
   edu.stanford.nlp.sempre.Session                    -> edu.stanford.nlp.sempre.DateValue                  DateValue.class
   edu.stanford.nlp.sempre.Session                    -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.Session                    -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.Session                    -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.Session                    -> edu.stanford.nlp.sempre.Value                      Value.class
SimpleAnalyzer.class -> LanguageAnalyzer$Options.class
SimpleAnalyzer.class -> LanguageAnalyzer.class
SimpleAnalyzer.class -> LanguageInfo.class
   edu.stanford.nlp.sempre.SimpleAnalyzer             -> edu.stanford.nlp.sempre.LanguageAnalyzer           LanguageAnalyzer.class
   edu.stanford.nlp.sempre.SimpleAnalyzer             -> edu.stanford.nlp.sempre.LanguageAnalyzer$Options   LanguageAnalyzer$Options.class
   edu.stanford.nlp.sempre.SimpleAnalyzer             -> edu.stanford.nlp.sempre.LanguageInfo               LanguageInfo.class
SimpleLexicon$Entry.class -> Formula.class
SimpleLexicon$Entry.class -> SemType.class
SimpleLexicon$Entry.class -> SimpleLexicon.class
   edu.stanford.nlp.sempre.SimpleLexicon$Entry        -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.SimpleLexicon$Entry        -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.SimpleLexicon$Entry        -> edu.stanford.nlp.sempre.SimpleLexicon              SimpleLexicon.class
SimpleLexicon$Options.class -> SimpleLexicon.class
   edu.stanford.nlp.sempre.SimpleLexicon$Options      -> edu.stanford.nlp.sempre.SimpleLexicon              SimpleLexicon.class
SimpleLexicon.class -> Formula.class
SimpleLexicon.class -> Json.class
SimpleLexicon.class -> SemType.class
SimpleLexicon.class -> SimpleLexicon$Entry.class
SimpleLexicon.class -> SimpleLexicon$Options.class
SimpleLexicon.class -> TypeInference.class
   edu.stanford.nlp.sempre.SimpleLexicon              -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.SimpleLexicon              -> edu.stanford.nlp.sempre.Json                       Json.class
   edu.stanford.nlp.sempre.SimpleLexicon              -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.SimpleLexicon              -> edu.stanford.nlp.sempre.SimpleLexicon$Entry        SimpleLexicon$Entry.class
   edu.stanford.nlp.sempre.SimpleLexicon              -> edu.stanford.nlp.sempre.SimpleLexicon$Options      SimpleLexicon$Options.class
   edu.stanford.nlp.sempre.SimpleLexicon              -> edu.stanford.nlp.sempre.TypeInference              TypeInference.class
SimpleLexiconFn$MyDerivationStream.class -> Derivation$Builder.class
SimpleLexiconFn$MyDerivationStream.class -> Derivation.class
SimpleLexiconFn$MyDerivationStream.class -> Example.class
SimpleLexiconFn$MyDerivationStream.class -> FeatureExtractor.class
SimpleLexiconFn$MyDerivationStream.class -> FeatureVector.class
SimpleLexiconFn$MyDerivationStream.class -> Formula.class
SimpleLexiconFn$MyDerivationStream.class -> MultipleDerivationStream.class
SimpleLexiconFn$MyDerivationStream.class -> SemType.class
SimpleLexiconFn$MyDerivationStream.class -> SemanticFn$Callable.class
SimpleLexiconFn$MyDerivationStream.class -> SemanticFn$Options.class
SimpleLexiconFn$MyDerivationStream.class -> SemanticFn.class
SimpleLexiconFn$MyDerivationStream.class -> SimpleLexicon$Entry.class
SimpleLexiconFn$MyDerivationStream.class -> SimpleLexicon.class
SimpleLexiconFn$MyDerivationStream.class -> SimpleLexiconFn.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.Derivation$Builder         Derivation$Builder.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.FeatureExtractor           FeatureExtractor.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.FeatureVector              FeatureVector.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.MultipleDerivationStream   MultipleDerivationStream.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.SemanticFn$Options         SemanticFn$Options.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.SimpleLexicon              SimpleLexicon.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.SimpleLexicon$Entry        SimpleLexicon$Entry.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream -> edu.stanford.nlp.sempre.SimpleLexiconFn            SimpleLexiconFn.class
SimpleLexiconFn$Options.class -> SimpleLexiconFn.class
   edu.stanford.nlp.sempre.SimpleLexiconFn$Options    -> edu.stanford.nlp.sempre.SimpleLexiconFn            SimpleLexiconFn.class
SimpleLexiconFn.class -> DerivationStream.class
SimpleLexiconFn.class -> Example.class
SimpleLexiconFn.class -> Formula.class
SimpleLexiconFn.class -> SemType.class
SimpleLexiconFn.class -> SemanticFn$Callable.class
SimpleLexiconFn.class -> SemanticFn.class
SimpleLexiconFn.class -> SimpleLexicon$Entry.class
SimpleLexiconFn.class -> SimpleLexicon.class
SimpleLexiconFn.class -> SimpleLexiconFn$MyDerivationStream.class
SimpleLexiconFn.class -> SimpleLexiconFn$Options.class
   edu.stanford.nlp.sempre.SimpleLexiconFn            -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.SimpleLexiconFn            -> edu.stanford.nlp.sempre.Example                    Example.class
   edu.stanford.nlp.sempre.SimpleLexiconFn            -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.SimpleLexiconFn            -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.SimpleLexiconFn            -> edu.stanford.nlp.sempre.SemanticFn                 SemanticFn.class
   edu.stanford.nlp.sempre.SimpleLexiconFn            -> edu.stanford.nlp.sempre.SemanticFn$Callable        SemanticFn$Callable.class
   edu.stanford.nlp.sempre.SimpleLexiconFn            -> edu.stanford.nlp.sempre.SimpleLexicon              SimpleLexicon.class
   edu.stanford.nlp.sempre.SimpleLexiconFn            -> edu.stanford.nlp.sempre.SimpleLexicon$Entry        SimpleLexicon$Entry.class
   edu.stanford.nlp.sempre.SimpleLexiconFn            -> edu.stanford.nlp.sempre.SimpleLexiconFn$MyDerivationStream SimpleLexiconFn$MyDerivationStream.class
   edu.stanford.nlp.sempre.SimpleLexiconFn            -> edu.stanford.nlp.sempre.SimpleLexiconFn$Options    SimpleLexiconFn$Options.class
SingleDerivationStream$1.class -> Derivation.class
SingleDerivationStream$1.class -> SingleDerivationStream.class
   edu.stanford.nlp.sempre.SingleDerivationStream$1   -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.SingleDerivationStream$1   -> edu.stanford.nlp.sempre.SingleDerivationStream     SingleDerivationStream.class
SingleDerivationStream.class -> Derivation.class
SingleDerivationStream.class -> DerivationStream.class
SingleDerivationStream.class -> SingleDerivationStream$1.class
   edu.stanford.nlp.sempre.SingleDerivationStream     -> edu.stanford.nlp.sempre.Derivation                 Derivation.class
   edu.stanford.nlp.sempre.SingleDerivationStream     -> edu.stanford.nlp.sempre.DerivationStream           DerivationStream.class
   edu.stanford.nlp.sempre.SingleDerivationStream     -> edu.stanford.nlp.sempre.SingleDerivationStream$1   SingleDerivationStream$1.class
StringValue.class -> Value.class
   edu.stanford.nlp.sempre.StringValue                -> edu.stanford.nlp.sempre.Value                      Value.class
SuperlativeFormula$Mode.class -> SuperlativeFormula.class
   edu.stanford.nlp.sempre.SuperlativeFormula$Mode    -> edu.stanford.nlp.sempre.SuperlativeFormula         SuperlativeFormula.class
SuperlativeFormula.class -> Formula.class
SuperlativeFormula.class -> SuperlativeFormula$Mode.class
   edu.stanford.nlp.sempre.SuperlativeFormula         -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.SuperlativeFormula         -> edu.stanford.nlp.sempre.SuperlativeFormula$Mode    SuperlativeFormula$Mode.class
TableValue.class -> Value.class
TableValue.class -> Values.class
   edu.stanford.nlp.sempre.TableValue                 -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.TableValue                 -> edu.stanford.nlp.sempre.Values                     Values.class
TargetValuePreprocessor$Options.class -> TargetValuePreprocessor.class
   edu.stanford.nlp.sempre.TargetValuePreprocessor$Options -> edu.stanford.nlp.sempre.TargetValuePreprocessor    TargetValuePreprocessor.class
TargetValuePreprocessor.class -> IdentityTargetValuePreprocessor.class
TargetValuePreprocessor.class -> SempreUtils.class
TargetValuePreprocessor.class -> TargetValuePreprocessor$Options.class
TargetValuePreprocessor.class -> Value.class
   edu.stanford.nlp.sempre.TargetValuePreprocessor    -> edu.stanford.nlp.sempre.IdentityTargetValuePreprocessor IdentityTargetValuePreprocessor.class
   edu.stanford.nlp.sempre.TargetValuePreprocessor    -> edu.stanford.nlp.sempre.SempreUtils                SempreUtils.class
   edu.stanford.nlp.sempre.TargetValuePreprocessor    -> edu.stanford.nlp.sempre.TargetValuePreprocessor$Options TargetValuePreprocessor$Options.class
   edu.stanford.nlp.sempre.TargetValuePreprocessor    -> edu.stanford.nlp.sempre.Value                      Value.class
TimeValue.class -> Value.class
   edu.stanford.nlp.sempre.TimeValue                  -> edu.stanford.nlp.sempre.Value                      Value.class
TopSemType.class -> SemType.class
   edu.stanford.nlp.sempre.TopSemType                 -> edu.stanford.nlp.sempre.SemType                    SemType.class
Trie.class -> Rule.class
   edu.stanford.nlp.sempre.Trie                       -> edu.stanford.nlp.sempre.Rule                       Rule.class
TypeInference$1.class -> TypeInference.class
   edu.stanford.nlp.sempre.TypeInference$1            -> edu.stanford.nlp.sempre.TypeInference              TypeInference.class
TypeInference$Env.class -> SemType.class
TypeInference$Env.class -> TypeInference$Options.class
TypeInference$Env.class -> TypeInference.class
TypeInference$Env.class -> TypeLookup.class
   edu.stanford.nlp.sempre.TypeInference$Env          -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.TypeInference$Env          -> edu.stanford.nlp.sempre.TypeInference              TypeInference.class
   edu.stanford.nlp.sempre.TypeInference$Env          -> edu.stanford.nlp.sempre.TypeInference$Options      TypeInference$Options.class
   edu.stanford.nlp.sempre.TypeInference$Env          -> edu.stanford.nlp.sempre.TypeLookup                 TypeLookup.class
TypeInference$Options.class -> TypeInference.class
   edu.stanford.nlp.sempre.TypeInference$Options      -> edu.stanford.nlp.sempre.TypeInference              TypeInference.class
TypeInference$TypeException.class -> TypeInference$1.class
TypeInference$TypeException.class -> TypeInference.class
   edu.stanford.nlp.sempre.TypeInference$TypeException -> edu.stanford.nlp.sempre.TypeInference              TypeInference.class
   edu.stanford.nlp.sempre.TypeInference$TypeException -> edu.stanford.nlp.sempre.TypeInference$1            TypeInference$1.class
TypeInference.class -> AggregateFormula.class
TypeInference.class -> ArithmeticFormula.class
TypeInference.class -> CallFormula.class
TypeInference.class -> CallTypeInfo.class
TypeInference.class -> CanonicalNames.class
TypeInference.class -> DateValue.class
TypeInference.class -> Formula.class
TypeInference.class -> Formulas.class
TypeInference.class -> FuncSemType.class
TypeInference.class -> JoinFormula.class
TypeInference.class -> LambdaFormula.class
TypeInference.class -> MarkFormula.class
TypeInference.class -> MergeFormula.class
TypeInference.class -> NameValue.class
TypeInference.class -> NotFormula.class
TypeInference.class -> NumberValue.class
TypeInference.class -> ReverseFormula.class
TypeInference.class -> SemType.class
TypeInference.class -> SempreUtils.class
TypeInference.class -> StringValue.class
TypeInference.class -> SuperlativeFormula.class
TypeInference.class -> TimeValue.class
TypeInference.class -> TypeInference$1.class
TypeInference.class -> TypeInference$Env.class
TypeInference.class -> TypeInference$Options.class
TypeInference.class -> TypeInference$TypeException.class
TypeInference.class -> TypeLookup.class
TypeInference.class -> Value.class
TypeInference.class -> ValueFormula.class
TypeInference.class -> VariableFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.AggregateFormula           AggregateFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.ArithmeticFormula          ArithmeticFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.CallFormula                CallFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.CallTypeInfo               CallTypeInfo.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.CanonicalNames             CanonicalNames.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.DateValue                  DateValue.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.Formula                    Formula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.Formulas                   Formulas.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.FuncSemType                FuncSemType.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.JoinFormula                JoinFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.LambdaFormula              LambdaFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.MarkFormula                MarkFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.MergeFormula               MergeFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.NameValue                  NameValue.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.NotFormula                 NotFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.NumberValue                NumberValue.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.ReverseFormula             ReverseFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.SempreUtils                SempreUtils.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.StringValue                StringValue.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.SuperlativeFormula         SuperlativeFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.TimeValue                  TimeValue.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.TypeInference$1            TypeInference$1.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.TypeInference$Env          TypeInference$Env.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.TypeInference$Options      TypeInference$Options.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.TypeInference$TypeException TypeInference$TypeException.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.TypeLookup                 TypeLookup.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.Value                      Value.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.ValueFormula               ValueFormula.class
   edu.stanford.nlp.sempre.TypeInference              -> edu.stanford.nlp.sempre.VariableFormula            VariableFormula.class
TypeLookup.class -> SemType.class
   edu.stanford.nlp.sempre.TypeLookup                 -> edu.stanford.nlp.sempre.SemType                    SemType.class
UnionSemType.class -> SemType.class
UnionSemType.class -> TopSemType.class
   edu.stanford.nlp.sempre.UnionSemType               -> edu.stanford.nlp.sempre.SemType                    SemType.class
   edu.stanford.nlp.sempre.UnionSemType               -> edu.stanford.nlp.sempre.TopSemType                 TopSemType.class
UriValue.class -> Value.class
   edu.stanford.nlp.sempre.UriValue                   -> edu.stanford.nlp.sempre.Value                      Value.class
Value$ValueComparator.class -> Value.class
   edu.stanford.nlp.sempre.Value$ValueComparator      -> edu.stanford.nlp.sempre.Value                      Value.class
Value.class -> Value$ValueComparator.class
Value.class -> Values.class
   edu.stanford.nlp.sempre.Value                      -> edu.stanford.nlp.sempre.Value$ValueComparator      Value$ValueComparator.class
   edu.stanford.nlp.sempre.Value                      -> edu.stanford.nlp.sempre.Values                     Values.class
ValueEvaluator.class -> Value.class
   edu.stanford.nlp.sempre.ValueEvaluator             -> edu.stanford.nlp.sempre.Value                      Value.class
ValueFormula.class -> NameValue.class
ValueFormula.class -> PrimitiveFormula.class
ValueFormula.class -> Value.class
   edu.stanford.nlp.sempre.ValueFormula               -> edu.stanford.nlp.sempre.NameValue                  NameValue.class
   edu.stanford.nlp.sempre.ValueFormula               -> edu.stanford.nlp.sempre.PrimitiveFormula           PrimitiveFormula.class
   edu.stanford.nlp.sempre.ValueFormula               -> edu.stanford.nlp.sempre.Value                      Value.class
Values.class -> BooleanValue.class
Values.class -> ContextValue.class
Values.class -> DateValue.class
Values.class -> DescriptionValue.class
Values.class -> ErrorValue.class
Values.class -> ListValue.class
Values.class -> NameValue.class
Values.class -> NumberValue.class
Values.class -> StringValue.class
Values.class -> TableValue.class
Values.class -> TimeValue.class
Values.class -> UriValue.class
Values.class -> Value.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.BooleanValue               BooleanValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.ContextValue               ContextValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.DateValue                  DateValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.DescriptionValue           DescriptionValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.ErrorValue                 ErrorValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.ListValue                  ListValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.NameValue                  NameValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.NumberValue                NumberValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.StringValue                StringValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.TableValue                 TableValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.TimeValue                  TimeValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.UriValue                   UriValue.class
   edu.stanford.nlp.sempre.Values                     -> edu.stanford.nlp.sempre.Value                      Value.class
VariableFormula.class -> PrimitiveFormula.class
   edu.stanford.nlp.sempre.VariableFormula            -> edu.stanford.nlp.sempre.PrimitiveFormula           PrimitiveFormula.class
```
