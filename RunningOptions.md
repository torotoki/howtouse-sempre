```
Usage:
  FeatureVector.ignoreZeroWeight < bool> : When logging, ignore features with zero weight [false]
  FeatureVector.logFeaturesLimit <  int> : Log only this number of top and bottom features [2147483647]
  FloatingParser.maxDepth        <  int> :  [10]
  FloatingParser.defaultIsFloating < bool> :  [true]
  FloatingParser.useAnchorsOnce  < bool> : Flag specifying whether anchored spans/tokens can only be used once in a derivation [false]
  FloatingParser.consecutiveRules < bool> : Flag specifying whether floating rules are allowed to be applied consecutively [true]
  FloatingParser.executeAllDerivations < bool> : Whether to always execute the derivation [false]
  FloatingParser.printPredictedUtterances < bool> : Whether to output a file with all utterances predicted [false]
  FloatingParser.useSizeInsteadOfDepth < bool> : Put a limit on formula size instead of formula depth [false]
  FloatingParser.trainBeamSize   <  int> : Custom beam size at training time (default = Parser.beamSize) [-1]
  ParserState.customExpectedCounts < enum> : Use a custom distribution for computing expected counts [NONE] NONE|UNIFORM|TOP|RANDOM
  ParserState.pruneByProbDiff    < bool> : Whether to prune based on probability difference [false]
  ParserState.probDiffPruningThresh <  dbl> : Difference in probability for pruning by prob diff [100.0]
  Server.port                    <  int> :  [8400]
  Server.numThreads              <  int> :  [4]
  Server.title                   <  str> :  [SEMPRE Demo]
  Server.headerPath              <  str> :  []
  Server.basePath                <  str> :  [demo-www]
  Server.verbose                 <  int> :  [1]
  Server.htmlVerbose             <  int> :  [1]
  log.maxIndLevel                <  int> : Maximum indent level. [2147483647]
  log.msPerLine                  <  int> : Maximum number of milliseconds between consecutive lines of output. [0]
  log.file                       <  str> : File to write log. []
  log.stdout                     < bool> : Whether to output to the console. [true]
  log.note                       <  str> : Dummy placeholder for a comment []
  log.maxPrintErrors             <  int> : Maximum number of errors (via error()) to print [10000]
  log.maxPrintWarnings           <  int> : Maximum number of warnings (via warning()) to print [10000]
  Builder.inParamsPath           <  str> :  []
  Builder.executor               <  str> :  [JavaExecutor]
  Builder.valueEvaluator         <  str> :  [ExactValueEvaluator]
  Builder.parser                 <  str> :  [BeamParser]
  Derivation.showValues          < bool> : When printing derivations, to show values (could be quite verbose) [true]
  Derivation.showFirstValue      < bool> : When printing derivations, to show the first value (ignored when showValues is set) [false]
  Derivation.showTypes           < bool> : When printing derivations, to show types [true]
  Derivation.showRules           < bool> : When printing derivations, to show rules [false]
  Derivation.showUtterance       < bool> : When printing derivations, to show canonical utterance [false]
  Derivation.showExecutions      < bool> : When executing, show formulae (for debugging) [false]
  MergeFn.hardTypeCheck          < bool> : whether to do a hard type-check [true]
  MergeFn.showTypeCheckFailures  < bool> :  [false]
  MergeFn.verbose                <  int> : Verbose [0]
  ReinforcementParser.efficientCoarsePrune < bool> : Whether to do coarse pruning [true]
  ReinforcementParser.multiplicativeBonus <  dbl> : Whether to do importance sampling [1000.0]
  ReinforcementParser.numOfSamplesPerExample <  int> : Number of samples [1]
  ReinforcementParser.updateGradientForCorrectMovesOnly < bool> : Whether to update gradient only for correct moves [true]
  ReinforcementParser.lowProb    <  dbl> : Low probability for which we don't unroll the stream [0.01]
  ReinforcementParser.simulateNonRlObjective < bool> : Whether to simulate the log liklihood objective [false]
  ReinforcementParser.alwaysUnroll < bool> : Whether to always unroll (even at test time) [false]
  TypeInference.verbose          <  int> : Verbosity level [1]
  TypeInference.typeLookup       <  str> : Class for looking up types [NullTypeLookup]
  FeatureExtractor.featureDomains <  unk> : Set of feature domains to include [[]]
  FeatureExtractor.featureComputers <  unk> : Set of feature computer classes to load [[DerivOpCountFeatureComputer]]
  FeatureExtractor.disableDenotationFeatures < bool> : Disable denotation features [false]
  FeatureExtractor.useAllFeatures < bool> : Use all possible features, regardless of what featureDomains says [false]
  FeatureExtractor.maxBigramDistance <  int> : For bigram features in paraphrased utterances, maximum distance to consider [3]
  FeatureExtractor.lexicalBigramParaphrase < bool> : Whether or not paraphrasing and bigram features should be lexicalized [true]
  BeamParser.maxNewTreesPerSpan  <  int> :  [2147483647]
  FuzzyMatchFn.verbose           <  int> :  [0]
  DerivOpCountFeatureComputer.countBasicOnly < bool> : Count only basic categories and SemanticFns [true]
  LanguageAnalyzer.languageAnalyzer <  str> :  [SimpleAnalyzer]
  LanguageAnalyzer.lowerCaseTokens < bool> : Whether to convert tokens in the utterance to lowercase [true]
  JavaExecutor.convertNumberValues < bool> : Whether to convert NumberValue to int/double [true]
  JavaExecutor.printStackTrace   < bool> : Print stack trace on exception [false]
  SelectFn.verbose               <  int> : Verbose [0]
  Dataset.inPaths                <str2*> : Paths to read input files (format: <group>:<file>) []
  Dataset.maxExamples            <str2*> : Maximum number of examples to read []
  Dataset.trainFrac              <  dbl> : Fraction of trainExamples (from the beginning) to keep for training [1.0]
  Dataset.devFrac                <  dbl> : Fraction of trainExamples (from the end) to keep for development [0.0]
  Dataset.splitRandom            < rand> : Used to randomly divide training examples [1]
  Dataset.splitDevFromTrain      < bool> : whether to split dev from train [true]
  Dataset.maxTokens              <  int> : Only keep examples which have at most this number of tokens [2147483647]
  Dataset.globalGraphPath        <  str> : Path to a knowledge graph that will be uploaded as global context []
  JoinFn.verbose                 <  int> : Verbose [0]
  JoinFn.showTypeCheckFailures   < bool> :  [false]
  JoinFn.typeInference           < bool> :  [true]
  JoinFn.specializedTypeCheck    < bool> :  [false]
  TargetValuePreprocessor.targetValuePreprocessor <  str> :  []
  SimpleLexicon.inPaths          <  unk> : Path to load lexicon files from []
  SimpleLexicon.matchSuffixTypes <  unk> : Types to allow suffix (last word) matche (for people names []
  Params.defaultWeight           <  dbl> : By default, all features have this weight [0.0]
  Params.initWeightsRandomly     < bool> : Randomly initialize the weights [false]
  Params.initRandom              < rand> : Randomly initialize the weights [1]
  Params.initStepSize            <  dbl> : Initial step size [1.0]
  Params.stepSizeReduction       <  dbl> : How fast to reduce the step size [0.0]
  Params.adaptiveStepSize        < bool> : Use the AdaGrad algorithm (different step size for each coordinate) [true]
  Params.dualAveraging           < bool> : Use dual averaging [false]
  Params.l1Reg                   <  str> : Whether to do lazy l1 reg updates [none]
  Params.l1RegCoeff              <  dbl> : L1 reg coefficient [0.0]
  Params.lazyL1FullUpdateFreq    <  int> : Lazy L1 full update frequency [5000]
  Grammar.inPaths                <  unk> :  []
  Grammar.tags                   <  unk> : Variables which are used to interpret the grammar file []
  Grammar.binarizeRules          < bool> :  [true]
  SemTypeHierarchy.failOnUnknownTypes < bool> : Throw an error if the type is not registered in the type hierarchy. [false]
  Learner.maxTrainIters          <  int> : Number of iterations to train [0]
  Learner.batchSize              <  int> : When using mini-batch updates for SGD, this is the batch size [1]
  Learner.outputPredDerivations  < bool> : Write predDerivations to examples file (huge) [false]
  Learner.dumpFeaturesAndCompatibility < bool> : Dump all features and compatibility scores [false]
  Learner.addFeedback            < bool> : Whether to add feedback [false]
  Learner.sortOnFeedback         < bool> : Whether to sort on feedback [true]
  Learner.verbose                <  int> : Verbosity [0]
  Learner.initialization         <  unk> : Initialize with these parameters []
  Learner.updateWeights          < bool> : whether to update weights [true]
  Learner.checkGradient          < bool> : whether to check gradient [false]
  Parser.printAllPredictions     < bool> : For debugging, whether to print out all the predicted derivations [false]
  Parser.maxPrintedPredictions   <  int> : Maximal number of predictions to print [2147483647]
  Parser.maxPrintedTrue          <  int> : Maximal number of correct predictions to print [2147483647]
  Parser.coarsePrune             < bool> : Use a coarse pass to prune the chart before full parsing [false]
  Parser.verbose                 <  int> : How much output to print [0]
  Parser.executeTopFormulaOnly   < bool> : Execute only top formula to be cheap (hack at test time for fast demo) [false]
  Parser.visualizeChartFilling   < bool> : Whether to output chart filling visualization (huge file!) [false]
  Parser.beamSize                <  int> : Keep this number of derivations per cell (exact use depends on the parser) [200]
  Parser.partialReward           < bool> : Whether to update based on partial reward (for learning) [true]
  Parser.unrollStream            < bool> : Whether to unroll derivation streams (applies to lazy parsers) [false]
  Parser.derivationScoreNoise    <  dbl> : Inject random noise into the score (to mix things up a bit) [0.0]
  Parser.derivationScoreRandom   < rand> : Source of random noise [1]
  Parser.pruneErrorValues        < bool> : Prune away error denotations [false]
  Parser.dumpAllFeatures         < bool> : Dump all features (for debugging) [false]
  Master.scriptPaths             <  unk> : Execute these commands before starting []
  Master.commands                <  unk> : Execute these commands before starting (after scriptPaths) []
  Master.logPath                 <  str> : Write a log of this session to this path []
  Master.printHelp               < bool> : Print help on startup [true]
  Master.contextMaxExchanges     <  int> : Number of exchanges to keep in the context [0]
  Master.onlineLearnExamples     < bool> : Online update weights on new examples. [true]
  Master.newExamplesPath         <  str> : Write out new examples to this directory []
  Master.newParamsPath           <  str> : Write out new parameters to this directory []
  Master.newGrammarPath          <  str> : Write out new grammar rules []
  SimpleLexiconFn.maxEntityEntries <  int> : Number of entities to return from entity lexicon [100]
  SimpleLexiconFn.verbose        <  int> : Verbosity level [0]
  NumberFn.unitless              < bool> : Omit units [false]
  NumberFn.alsoTestByConversion  < bool> : Also test numbers by try converting to float (instead of using NER tags) [false]
  SemanticFn.trackLocalChoices   < bool> : Whether or not to add to Derivation.localChoices during function application (for debugging only). [false]
  DerivationPruner.pruningStrategies <  unk> :  []
  DerivationPruner.pruningComputers <  unk> :  []
  DerivationPruner.pruningVerbosity <  int> :  [0]
  DerivationPruner.maxNumValues  <  int> :  [10]
  Main.interactive               < bool> :  [false]
  Main.server                    < bool> :  [false]
  exec.monitor                   < bool> : Whether to create a thread to monitor the status of this execution. [true]
  exec.execDir                   <  str> : Directory to put all output files; if empty, use execPoolDir. []
  exec.execPoolDir               <  str> : Directory which contains all the executions. []
  exec.overwriteExecDir          < bool> : Overwrite the contents of the execDir if it doesn't exist (e.g., when running a thunk). [false]
  exec.printOptionsAndExit       < bool> : Simply print options and exit. [false]
  exec.miscOptions               < str*> : Miscellaneous options (written to options.map and output.map, displayed in servlet); example: a=3 b=4 []
  exec.addToView                 < str*> : Name of the view to add this execution to in the servlet (simply creates an addToView file). []
  exec.charEncoding              <  str> : Character encoding []
  exec.jarFiles                  < str*> : Name of jar files to load prior to execution.  This is so that when the JARs change underneath us, we don't crash. []
  exec.startMainTrack            < bool> : Whether to wrap everything around a main() track [true]
```
