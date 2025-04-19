class Currency:
    def __init__(
        self,
        code,
        singular,
        dual,
        plural,
        fraction_singular,
        fraction_dual,
        fraction_plural,
        part_precision=2,
        en_name="Unknown Currency",
        en_fraction_name="subunit"
    ):
        self.code = code
        self.singular = singular
        self.dual = dual
        self.plural = plural
        self.fraction_singular = fraction_singular
        self.fraction_dual = fraction_dual
        self.fraction_plural = fraction_plural
        self.part_precision = part_precision
        self.en_name = en_name
        self.en_fraction_name = en_fraction_name
