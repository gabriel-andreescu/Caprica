Scriptname ConditionalReturns

Int Function DebugValue() Global DebugOnly
    Return 42
EndFunction

Float Function BetaValue() Global BetaOnly
    Return 3.5
EndFunction

Int Function ReadDebug() Global
    Return DebugValue()
EndFunction

Float Function ReadBeta() Global
    Return BetaValue()
EndFunction
