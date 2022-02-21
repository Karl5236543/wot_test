from django.db import models

class BattleLog(models.Model):
    battle_time = models.IntegerField()
    win_resp = models.CharField(max_length=1, choices=[('n', 'nizni'), ('v', 'verhni')])

    def __str__(self):
        return f"{self.battle_time} - {self.win_resp}"
