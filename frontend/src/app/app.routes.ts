import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ActividadesDashboardComponent } from './actividades-dashboard.component';

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: '', component: ActividadesDashboardComponent },
];
