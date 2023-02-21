from yaramo.model import Topology
from yaramo.vacancy_section import VacancySection

class VacancySectionGenerator:
    def __init__(self, topology: Topology) -> "VacancySectionGenerator":
        self.topology = topology

    def generate(self):
        for edge in self.topology.edges.values():
            if not edge.vacancy_section:
                vacancy_section = VacancySection()
                edge.vacancy_section = vacancy_section
                self.topology.add_vacancy_section(vacancy_section)
        
        for route in self.topology.routes.values():
            for edge in route.edges:
                if edge.vacancy_section:
                    route.vacancy_sections.add(edge.vacancy_section)
