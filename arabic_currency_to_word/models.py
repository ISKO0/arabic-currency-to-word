class Currency:
    def __init__(self, code, singular, dual, plural, fraction_singular, fraction_dual, fraction_plural, part_precision=2):
        self.code = code
        self.singular = singular
        self.dual = dual
        self.plural = plural
        self.fraction_singular = fraction_singular
        self.fraction_dual = fraction_dual
        self.fraction_plural = fraction_plural
        self.part_precision = part_precision
