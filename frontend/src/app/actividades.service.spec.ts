
import { TestBed } from '@angular/core/testing';
import { HttpClientTestingModule } from '@angular/common/http/testing';
import { ActividadesService } from './actividades.service';

describe('ActividadesService', () => {
  let service: ActividadesService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]
    });
    service = TestBed.inject(ActividadesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
