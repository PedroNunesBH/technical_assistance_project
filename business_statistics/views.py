from django.views.generic import TemplateView
from devices.models import Devices
from technicals.models import Technicals


class TechnicalsStatisticsView(TemplateView):
    template_name = 'technicals_statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        devices_list = Devices.objects.all()
        total_of_devices = 0
        total_billing = 0  # faturamento total até o momento
        for device in devices_list:
            if device.status != "Em Orçamento" and device.status != "Aguardando Aprovação":
                total_billing += float(device.repair_price)

        technicals_list = Technicals.objects.all()  # Captura todos os tecnicos do model Technicals
        number_of_employees = 0
        total_wages = 0
        for technical in technicals_list:  # percorre cada elemento da lista
            number_of_employees += 1  # para cada tecnico adiciona 1 no numero de funcionarios
            total_wages += technical.salary  # adiciona o salario de cada tecnico no total de salarios

        context["number_of_employees"] = number_of_employees
        context["total_wages"] = total_wages
        context["total_billing"] = total_billing
        return context
