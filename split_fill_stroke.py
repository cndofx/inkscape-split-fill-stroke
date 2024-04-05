import inkex

class SplitFillStroke(inkex.EffectExtension):
    def effect(self):
        layer = self.svg.get_current_layer()
        for orig in self.svg.selected:
            new = orig.duplicate()
            new.style['fill'] = 'none'
            orig.style['stroke'] = 'none'
            layer.append(new)

if __name__ == '__main__':
    SplitFillStroke().run()