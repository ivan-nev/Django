from django.db import models
# from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Датчик')
    description = models.CharField(max_length=80, verbose_name='Описание')
    foto = models.ImageField(blank=True, null=True, verbose_name='фотография')
    # foto = ProcessedImageField(blank=True, null=True, verbose_name='фотография',
    #                                        processors=[ResizeToFill(100, 50)],
    #                                        format='JPEG',
    #                                        options={'quality': 60})

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.name} - {self.description}'

    # def save(self):
    #     # Opening the uploaded image
    #     im = Image.open(self.foto)
    #     output = BytesIO()
    #     # Resize/modify the image
    #     im = im.resize((100, 100))
    #     # after modifications, save it to the output
    #     im.save(output, format='JPEG', quality=90)
    #     output.seek(0)
    #     # change the imagefield value to be the newley modifed image value
    #     self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.image.name.split('.')[0], 'image/jpeg',
    #                                     sys.getsizeof(output), None)
    #     super(Report_item, self).save()


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=4, decimal_places=1, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата')

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'{self.sensor} -- {self.temperature}'
