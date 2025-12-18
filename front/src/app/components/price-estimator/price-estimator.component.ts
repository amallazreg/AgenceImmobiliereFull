import { Component } from '@angular/core';
import { PredictionService } from '../../services/prediction.service';

@Component({
  selector: 'app-price-estimator',
  templateUrl: './price-estimator.component.html',
  styleUrls: ['./price-estimator.component.css']
})
export class PriceEstimatorComponent {

  surface = 0;
  type = 'House';
  transaction = 'a vendre';
  localisation = 'Tunis';

  estimatedPrice: number | null = null;
  isLoading = false;

  constructor(private predictionService: PredictionService) {}

  estimate() {
    // Validation basique
    if (!this.surface || this.surface <= 0) {
      alert('Veuillez entrer une surface valide');
      return;
    }

    // Activation de l'état de chargement
    this.isLoading = true;
    this.estimatedPrice = null;

    const payload: any = {
      surface: this.surface
    };

    payload['type_' + this.type] = 1;
    payload['transaction_' + this.transaction] = 1;
    payload['localisation_' + this.localisation] = 1;

    this.predictionService.predictPrice(payload)
      .subscribe({
        next: (res) => {
          // Simulation d'un délai minimum pour l'animation
          setTimeout(() => {
            this.estimatedPrice = res.estimated_price;
            this.isLoading = false;
          }, 500);
        },
        error: (err) => {
          console.error('Erreur lors de l\'estimation:', err);
          this.isLoading = false;
          alert('Une erreur s\'est produite. Veuillez réessayer.');
        }
      });
  }
}