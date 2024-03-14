from django.views.generic import TemplateView
from django.db.models import Sum, Count
from devices.models import Devices
from technicals.models import Technicals


class TechnicalsStatisticsView(TemplateView):
    template_name = 'technicals_statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Consulta para calcular o faturamento total excluindo dispositivos em orçamento e aguardando aprovação
        total_billing = Devices.objects.exclude(status__in=["Em Orçamento", "Aguardando Aprovação"]) \
                                       .aggregate(total=Sum('repair_price'))['total'] or 0

        repairs_number = Devices.objects.filter(status='Entregue').count()

        # Consulta para calcular o número total de técnicos por posição
        employees_by_position = Technicals.objects.values('employee_position') \
                                                    .annotate(count=Count('id')) \
                                                    .order_by('employee_position')
        positions_totals = {}

        for item in employees_by_position:
            position = item['employee_position']
            count = item['count']
            positions_totals[position] = count

        managers = positions_totals.get('Gerente', 0)  # Captura o valor da chave especificada ou retorna 0 se n houver
        technicals = positions_totals.get('Técnico', 0)
        attendants = positions_totals.get('Atendente', 0)

        # Cálculo do número total de funcionários e total de salários
        number_of_employees = sum(item['count'] for item in employees_by_position)
        total_wages = sum(technical.salary for technical in Technicals.objects.all())

        print(repairs_number)
        context["number_of_employees"] = number_of_employees
        context["total_wages"] = total_wages
        context["total_billing"] = total_billing
        context["managers"] = managers
        context["technicals"] = technicals
        context["attendants"] = attendants
        context["repairs_number"] = repairs_number
        return context
