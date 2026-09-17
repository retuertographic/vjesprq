# Compatibilidad para compilar en local con Ruby >= 3.2.
# GitHub Pages usa Jekyll 3.9 / Liquid 4.0.3, que todavía llaman a métodos "taint" eliminados de Ruby.
# Solo se carga desde herramientas/servir.sh; GitHub Pages no lo usa.
class Object
  def tainted?; false; end
  def taint; self; end
  def untaint; self; end
end
