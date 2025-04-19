from .models import Currency

currencies = {
    "SAR": Currency("SAR", "ريال", "ريالان", "ريالات", "هللة", "هللتان", "هللات", 2, "Saudi Riyal", "halala"),
    "USD": Currency("USD", "دولار", "دولاران", "دولارات", "سنت", "سنتان", "سنتات", 2, "US Dollar", "cent"),
    "EUR": Currency("EUR", "يورو", "يوروان", "يوروهات", "سنت", "سنتان", "سنتات", 2, "Euro", "cent"),
    "EGP": Currency("EGP", "جنيه", "جنيهان", "جنيهات", "قرش", "قرشان", "قروش", 2, "Egyptian Pound", "piastre"),
    "SYP": Currency("SYP", "ليرة", "ليرتان", "ليرات", "قرش", "قرشان", "قروش", 2, "Syrian Pound", "qirsh"),
    "IQD": Currency("IQD", "دينار", "ديناران", "دنانير", "فلس", "فلسان", "فلوس", 2, "Iraqi Dinar", "fils"),
    "JOD": Currency("JOD", "دينار", "ديناران", "دنانير", "فلس", "فلسان", "فلوس", 2, "Jordanian Dinar", "fils"),
    "KWD": Currency("KWD", "دينار", "ديناران", "دنانير", "فلس", "فلسان", "فلوس", 2, "Kuwaiti Dinar", "fils"),
    "AED": Currency("AED", "درهم", "درهمان", "دراهم", "فلس", "فلسان", "فلوس", 2, "UAE Dirham", "fils"),
    "GBP": Currency("GBP", "جنيه إسترليني", "جنيهان إسترلينيان", "جنيهات إسترلينية", "بنس", "بنسين", "بنسات", 2, "British Pound", "penny"),
    "TRY": Currency("TRY", "ليرة تركية", "ليرتان تركيتان", "ليرات تركية", "قرش", "قرشان", "قروش", 2, "Turkish Lira", "kuruş"),
    "ZAR": Currency("ZAR", "راند", "راندان", "راندات", "سنت", "سنتان", "سنتات", 2, "South African Rand", "cent"),
}
