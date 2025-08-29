from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

CATEGORIAS = [
          ('Todas las categorias', 'Todas las categorias'),
        ('Acompañamiento', 'Acompañamiento'),
    ('Administración de la Educación', 'Administración de la Educación'),
    ('Alfabetización', 'Alfabetización'),
    ('Aprendizaje', 'Aprendizaje'),
    ('Aprendizaje colaborativo', 'Aprendizaje colaborativo'),
    ('Aprendizaje significativo', 'Aprendizaje significativo'),
    ('Asociación de padres', 'Asociación de padres'),
    ('Calidad Docente', 'Calidad Docente'),
    ('Calidad Educativa', 'Calidad Educativa'),
    ('Cambio de carrera', 'Cambio de carrera'),
    ('Capacitación Docente', 'Capacitación Docente'),
    ('Característica del Docente', 'Característica del Docente'),
    ('Ciencias de la Naturaleza', 'Ciencias de la Naturaleza'),
    ('Ciencias Químicas', 'Ciencias Químicas'),
    ('Ciencias Sociales', 'Ciencias Sociales'),
    ('Clima laboral', 'Clima laboral'),
    ('Competencia Ambiental y de la Salud', 'Competencia Ambiental y de la Salud'),
    ('Competencia Autoestima y Desarrollo Personal', 'Competencia Autoestima y Desarrollo Personal'),
    ('Competencia Científico Tecnológica', 'Competencia Científico Tecnológica'),
    ('Competencia Comunicativa', 'Competencia Comunicativa'),
    ('Competencia Ética y Ciudadana', 'Competencia Ética y Ciudadana'),
    ('Competencia Lingüística', 'Competencia Lingüística'),
    ('Competencia Literaria', 'Competencia Literaria'),
    ('Competencia Pensamiento Lógico Creativo y Crítico', 'Competencia Pensamiento Lógico Creativo y Crítico'),
    ('Competencia Resolución de Problemas', 'Competencia Resolución de Problemas'),
    ('Competencias Educativas', 'Competencias Educativas'),
    ('Competencias fundamentales', 'Competencias fundamentales'),
    ('Comprensión lectora', 'Comprensión lectora'),
    ('Cultura organizacional', 'Cultura organizacional'),
    ('Curriculum', 'Curriculum'),
    ('Desempleo', 'Desempleo'),
    ('Deserción Escolar', 'Deserción Escolar'),
    ('Desarrollo Intelectual', 'Desarrollo Intelectual'),
    ('Didáctica', 'Didáctica'),
    ('Disciplina escolar', 'Disciplina escolar'),
    ('Educación', 'Educación'),
    ('Educación Artística', 'Educación Artística'),
    ('Educación Básica', 'Educación Básica'),
    ('Educación Cívica', 'Educación Cívica'),
    ('Educación de Adultos', 'Educación de Adultos'),
    ('Educación en Valores', 'Educación en Valores'),
    ('Educación Física', 'Educación Física'),
    ('Educación Inicial', 'Educación Inicial'),
    ('Educación no formal', 'Educación no formal'),
    ('Educación Secundaria', 'Educación Secundaria'),
    ('Educación socioemocional', 'Educación socioemocional'),
    ('Educación Superior', 'Educación Superior'),
    ('Educación Superior a Distancia', 'Educación Superior a Distancia'),
    ('Ejes Transversales (Ciencia y Tecnología)', 'Ejes Transversales (Ciencia y Tecnología)'),
    ('Ejes Transversales (Contexto Social y Natural)', 'Ejes Transversales (Contexto Social y Natural)'),
    ('Ejes Transversales (Creatividad y Desarrollo de los Talentos)', 'Ejes Transversales (Creatividad y Desarrollo de los Talentos)'),
    ('Ejes Transversales (Cultura Dominicana: Identidad y Diversidad)', 'Ejes Transversales (Cultura Dominicana: Identidad y Diversidad)'),
    ('Ejes Transversales (Democracia y Participación Ciudadana)', 'Ejes Transversales (Democracia y Participación Ciudadana)'),
    ('Ejes Transversales (Educación y Salud)', 'Ejes Transversales (Educación y Salud)'),
    ('Ejes Transversales (El Trabajo como Medio de Realización Personal y Base del Desarrollo)', 'Ejes Transversales (El Trabajo como Medio de Realización Personal y Base del Desarrollo)'),
    ('Elección de Estudios', 'Elección de Estudios'),
    ('Emprendimiento', 'Emprendimiento'),
    ('Enseñanza', 'Enseñanza'),
    ('Enseñanza y aprendizaje', 'Enseñanza y aprendizaje'),
    ('Errores metodológicos', 'Errores metodológicos'),
    ('Escolarización', 'Escolarización'),
    ('Estado Dominicano', 'Estado Dominicano'),
    ('Estadística Abandono Escolar', 'Estadística Abandono Escolar'),
    ('Estrategia de enseñanza y de aprendizaje', 'Estrategia de enseñanza y de aprendizaje'),
    ('Estrategias', 'Estrategias'),
    ('Estrategias de aprendizajes', 'Estrategias de aprendizajes'),
    ('Estrategias didácticas', 'Estrategias didácticas'),
    ('Estrategias lúdicas', 'Estrategias lúdicas'),
    ('Estrategias metodológicas', 'Estrategias metodológicas'),
    ('Estrategias pedagógica', 'Estrategias pedagógica'),
    ('Evaluación', 'Evaluación'),
    ('Evaluación Educativa', 'Evaluación Educativa'),
    ('Formación Continua', 'Formación Continua'),
    ('Formación Docente', 'Formación Docente'),
    ('Formación Integral Humana y Religiosa', 'Formación Integral Humana y Religiosa'),
    ('Formación Técnico Profesional', 'Formación Técnico Profesional'),
    ('Función polinomial', 'Función polinomial'),
    ('Gerencia Educativa', 'Gerencia Educativa'),
    ('Gestión Educativa', 'Gestión Educativa'),
    ('Habilidades motoras', 'Habilidades motoras'),
    ('Habilidades motrices', 'Habilidades motrices'),
    ('Inclusión Educativa', 'Inclusión Educativa'),
    ('Innovación Educativa', 'Innovación Educativa'),
    ('Innovaciones Educativas', 'Innovaciones Educativas'),
    ('Integración Familiar', 'Integración Familiar'),
    ('Integración Profesional', 'Integración Profesional'),
    ('Intervención Psicopedagógica', 'Intervención Psicopedagógica'),
    ('Investigación', 'Investigación'),
    ('Jornada extendida', 'Jornada extendida'),
    ('Lectoescritura', 'Lectoescritura'),
    ('Lengua Española', 'Lengua Española'),
    ('Lengua Española y Literatura', 'Lengua Española y Literatura'),
    ('Lenguaje matemático', 'Lenguaje matemático'),
    ('Lenguas Extranjeras', 'Lenguas Extranjeras'),
    ('Liderazgo', 'Liderazgo'),
    ('Jornada extendida', 'Jornada extendida'),
    ('Matemática', 'Matemática'),
    ('Metodología', 'Metodología'),
    ('Motivación', 'Motivación'),
    ('Necesidades Educativas Especiales', 'Necesidades Educativas Especiales'),
    ('Neurociencia', 'Neurociencia'),
    ('Nivel Inicial', 'Nivel Inicial'),
    ('Números complejos', 'Números complejos'),
    ('Orientación', 'Orientación'),
    ('Participación', 'Participación'),
    ('Participación Comunitaria', 'Participación Comunitaria'),
    ('Pedagogía', 'Pedagogía'),
    ('Perfil del estudiante', 'Perfil del estudiante'),
    ('Planeamiento Educativo', 'Planeamiento Educativo'),
    ('Planificación Educativa', 'Planificación Educativa'),
    ('Polinomios', 'Polinomios'),
    ('Programa de Estudios', 'Programa de Estudios'),
    ('Proyección Profesional', 'Proyección Profesional'),
    ('Pruebas Nacionales', 'Pruebas Nacionales'),
    ('Psicología', 'Psicología'),
    ('Psicopedagogía', 'Psicopedagogía'),
    ('Razonamiento Lógico', 'Razonamiento Lógico'),
    ('Recursos', 'Recursos'),
    ('Recursos Didácticos', 'Recursos Didácticos'),
    ('Recursos Financieros', 'Recursos Financieros'),
    ('Relación Maestro', 'Relación Maestro'),
    ('Rendimiento', 'Rendimiento'),
    ('Rendimiento académico', 'Rendimiento académico'),
    ('Responsabilidad social', 'Responsabilidad social'),
    ('Selección de Docentes', 'Selección de Docentes'),
    ('Socio Pedagogía', 'Socio Pedagogía'),
    ('Sociología', 'Sociología'),
    ('Supervisión', 'Supervisión'),
    ('Técnicas de enseñanza', 'Técnicas de enseñanza'),
    ('Tecnología de la Información y de la Comunicación (TICs)', 'Tecnología de la Información y de la Comunicación (TICs)'),
    ('Tecnología Educativa', 'Tecnología Educativa'),
    ('Teorema', 'Teorema'),
    ('Terapia Familiar', 'Terapia Familiar'),
    ('Transformación', 'Transformación'),
    ('Violencia', 'Violencia'),
    ('Álgebra', 'Álgebra'),
    ('Ecuación', 'Ecuación')

]

class AddTermForm(FlaskForm):
    codigo = StringField('Código', validators=[DataRequired(), Length(max=50)])
    termino = StringField('Término', validators=[DataRequired(), Length(max=255)])
    categoria = SelectField('Categ  oría', choices=CATEGORIAS, validators=[DataRequired()])
    term_es = TextAreaField('Definición (ES)', validators=[DataRequired()])
    term_en = TextAreaField('Definition (EN)', validators=[DataRequired()])
    term_fr = TextAreaField('Définition (FR)', validators=[DataRequired()])
    ejemplo1_es = TextAreaField('Ejemplo 1 (ES)')
    ejemplo1_en = TextAreaField('Example 1 (EN)')
    ejemplo1_fr = TextAreaField('Exemple 1 (FR)')
    ejemplo2_es = TextAreaField('Ejemplo 2 (ES)')
    ejemplo2_en = TextAreaField('Example 2 (EN)')
    ejemplo2_fr = TextAreaField('Exemple 2 (FR)')
    fuente = StringField('Fuente', validators=[Length(max=255)])
    observacion = TextAreaField('Observación')
    submit = SubmitField('Agregar')

    def __init__(self, lang='es', *args, **kwargs):
        super(AddTermForm, self).__init__(*args, **kwargs)

        all_langs = ['es', 'en', 'fr']
        for l in all_langs:
            if l != lang:
                getattr(self, f'term_{l}').validators = [v for v in getattr(self, f'term_{l}').validators if not isinstance(v, DataRequired)]
                getattr(self, f'ejemplo1_{l}').validators = []
                getattr(self, f'ejemplo2_{l}').validators = []

        labels = {
            'es': {
                'codigo': 'Código',
                'termino': 'Término',
                'categoria': 'Categoría',
                'definition': 'Definición',
                'example1': 'Ejemplo 1',
                'example2': 'Ejemplo 2',
                'fuente': 'Fuente',
                'observacion': 'Observación',
                'submit': 'Agregar'
            },
            'en': {
                'codigo': 'Code',
                'termino': 'Term',
                'categoria': 'Category',
                'definition': 'Definition',
                'example1': 'Example 1',
                'example2': 'Example 2',
                'fuente': 'Source',
                'observacion': 'Observation',
                'submit': 'Add'
            },
            'fr': {
                'codigo': 'Code',
                'termino': 'Terme',
                'categoria': 'Catégorie',
                'definition': 'Définition',
                'example1': 'Exemple 1',
                'example2': 'Exemple 2',
                'fuente': 'Source',
                'observacion': 'Observation',
                'submit': 'Ajouter'
            }
        }

        current_labels = labels.get(lang, labels['es'])

        self.codigo.label.text = current_labels['codigo']
        self.termino.label.text = current_labels['termino']
        self.categoria.label.text = current_labels['categoria']
        self.fuente.label.text = current_labels['fuente']
        self.observacion.label.text = current_labels['observacion']
        self.submit.label.text = current_labels['submit']

        definition_field = getattr(self, f'term_{lang}')
        example1_field = getattr(self, f'ejemplo1_{lang}')
        example2_field = getattr(self, f'ejemplo2_{lang}')
        definition_field.label.text = current_labels['definition']
        example1_field.label.text = current_labels['example1']
        example2_field.label.text = current_labels['example2']