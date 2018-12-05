from orders.models import BasketModel

def user_profile(requsest):  # можно добавить в любой апликейшин предварительно прописав в сетинге


        session_key = requsest.session.session_key
        if not session_key:
            requsest.session.cycle_key()  # cycle_key - создает ключ вручную если его нету

        # по етому ключу ищем какие товары есть в корзине
        sesiion_in_basket = BasketModel.objects.filter(session_key=session_key, is_active=True) # кверисет
        count = sesiion_in_basket.count() # количество кверисетов


        return locals()

