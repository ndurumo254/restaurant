from email.mime import image
from unicodedata import name
from django.db import models

# Create your models here.
class Item(models.Model):
    name=models.CharField(max_length=200)
    desc=models.CharField(max_length=100)
    price=models.CharField(max_length=200)
    image=models.CharField(max_length=2600, default="https://www.google.com/search?q=food+image+placeholder&rlz=1C1BNSD_enKE1009KE1009&sxsrf=ALiCzsarRo9M7c68guir666e4s0iKNfOJw:1655297357579&tbm=isch&source=iu&ictx=1&vet=1&fir=r4MyYWa6UxepTM%252CDE59x2KNdrhkvM%252C_%253Bjal7CZrCohPPcM%252CSht218MD2XkntM%252C_%253B7K26ALkHdMGaaM%252CpW-HFWw0VNMbnM%252C_%253BcAtq_o3hdy3hOM%252CPAwBzaJSiNcWRM%252C_%253B59Y8go7tPpJqKM%252C0k5rhoJHXvlkdM%252C_%253BKzlEw1u98W7EKM%252C75wDOX_EasD4oM%252C_%253BPPivKK91_GfBwM%252CQW5tfoGwTo7iLM%252C_%253B_f-j934pbgJPIM%252Ce1j17iealMc86M%252C_%253BRqBiIF11oAHY9M%252C5BMqhlvIKCC8fM%252C_%253BlUtB87N36x-N0M%252Cs7_BUA5iuaTEKM%252C_%253BoYzOxU9PMSIQJM%252Ce1j17iealMc86M%252C_%253BZAPW46T6JNMzyM%252Cs7_BUA5iuaTEKM%252C_%253B3gu7rag2AQnNmM%252C7RPpozL6R3FwOM%252C_%253ByGLiR58i_nBKdM%252CQW5tfoGwTo7iLM%252C_%253B-fO_excvO9BrdM%252C0RuYXFRXZuB68M%252C_&usg=AI4_-kSsDWrpZ3ok_OFU7eMpBhpEyBlOuA&sa=X&ved=2ahUKEwiaxPuXv6_4AhWRlP0HHYAfAQ4Q9QF6BAgKEAE#imgrc=lUtB87N36x-N0M")

    def __str__(self):
        return self.name